from yaml import safe_load
import logging

from utils.validator.platforms import validate_platforms
from utils.renderer import render_notification
from database import SessionLocal, engine
from config import settings
import utils.logging_config

from cruds.repo import get_unnotified_releases, update_release_notification_status
from models.repo import Repo
from utils.platforms.telegram import send_telegram_message
from utils.platforms.slack import send_slack_message
from utils.platforms.email import send_email


# Create DB session
def get_db_session():
    db_session = SessionLocal()
    try:
        logger.info("Establishing database connection")
        return db_session
    except:
        logger.error("Unable to connect to database")
        db_session.close()


if __name__ == "__main__":
    # Define logger
    logger = logging.getLogger(__name__)

    # Create tables [IF NOT EXISTS]
    logger.info("Initiating tables creation")
    Repo.metadata.create_all(bind=engine)

    # Load providers configuration
    with open(settings.PLATFORMS_FILE, "r") as file:
        # Read repos configuration file
        logger.info("Loading repositories file")
        config_dict = safe_load(file)

        # Validate providers configuration file
        repos_validation, err = validate_platforms(config_dict=config_dict)
        if err:
            logger.error("Unable to load repositories file")
            raise err

    # Load unnotified_releases
    repos = get_unnotified_releases(db_session=get_db_session())
    if not repos:
        logger.warning("No releases to be notified. Terminated...")
        exit(0)

    # Send notifications
    for platform in config_dict.keys():
        if platform == "email":
            logger.info("Sending email notifications...")
            for repo in repos:
                message_body = render_notification(
                    provider=repo.provider,
                    repo=repo.repo_name,
                    tag_name=repo.tag_name,
                    type=config_dict[platform]["message_type"],
                )
                send_email(
                    receiver_email=config_dict[platform]["receiver_email"],
                    message_body=message_body,
                    subject="Release Notification",
                    smtp_server=config_dict[platform]["smtp_server"],
                    user_email=config_dict[platform]["user_email"],
                    user_password=config_dict[platform]["user_password"],
                    port=config_dict[platform]["port"],
                )

        if platform == "slack":
            logger.info("Sending slack notifications...")
            for repo in repos:
                message_body = render_notification(
                    provider=repo.provider,
                    repo=repo.repo_name,
                    tag_name=repo.tag_name,
                    type=config_dict[platform]["message_type"],
                )
                send_slack_message(
                    bot_token=config_dict[platform]["bot_token"],
                    channel_id=config_dict[platform]["channel_id"],
                    message_body=message_body,
                )

        if platform == "telegram":
            logger.info("Sending telegram notifications...")
            for repo in repos:
                message_body = render_notification(
                    provider=repo.provider,
                    repo=repo.repo_name,
                    tag_name=repo.tag_name,
                    type=config_dict[platform]["message_type"],
                )
                send_telegram_message(
                    bot_token=config_dict[platform]["bot_token"],
                    chat_id=config_dict[platform]["chat_id"],
                    message_body=message_body,
                )

    # Flag repos for future deletion
    logger.info("Flagging notified releases")
    for repo in repos:
        update_release_notification_status(
            provider=repo.provider,
            repo_name=repo.repo_name,
            tag_name=repo.tag_name,
            db_session=get_db_session(),
        )

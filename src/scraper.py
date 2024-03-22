from yaml import safe_load
import logging

from utils.validator.providers import validate_providers
from database import SessionLocal, engine
import utils.logging_config
from config import settings

from utils.providers.github import get_github_latest_release
from utils.providers.gitlab import get_gitlab_latest_release
from cruds.repo import add_release
from models.repo import Repo


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
    with open(settings.PROVIDERS_FILE, "r") as file:
        # Read repos configuration file
        logger.info("Loading repositories file")
        config_dict = safe_load(file)

        # Validate providers configuration file
        repos_validation, err = validate_providers(config_dict=config_dict)
        if err:
            logger.error("Unable to load repositories file")
            raise err

    # Fetch providers data
    logger.info("Fetching repositories data")
    for provider in config_dict.keys():
        if provider == "github":
            for repo_name in config_dict["github"]:
                release_body = get_github_latest_release(repo_name)
                if release_body:
                    add_release(
                        provider=provider,
                        repo_name=repo_name,
                        tag_name=release_body["tag_name"],
                        release_body=release_body,
                        db_session=get_db_session(),
                    )

        if provider == "gitlab":
            for repo_name in config_dict["gitlab"]:
                release_body = get_gitlab_latest_release(repo_name)
                if release_body:
                    add_release(
                        provider=provider,
                        repo_name=repo_name,
                        tag_name=release_body["tag_name"],
                        release_body=release_body,
                        db_session=get_db_session(),
                    )

from yaml import safe_load
import logging

from utils.validator.repos import validate_repos
from utils.exc import EmptyReposFileError
import utils.logging_config
from database import SessionLocal, engine
from config import settings

from utils.providers.github import get_github_latest_release
from utils.providers.gitlab import get_gitlab_latest_release
from cruds.repo import add_release
from models.repo import Repo


# Create DB Session
def get_db_session():
    db_session = SessionLocal()
    try:
        return db_session
    except:
        db_session.close()


if __name__ == '__main__':
    # Define logger
    logger = logging.getLogger(__name__)
    
    # Create Tables [IF NOT EXISTS]
    logger.info("Initiating Tables Creation")
    Repo.metadata.create_all(bind=engine)


    # Load Repos Configuration
    with open(settings.REPOS_FILE, "r") as file:
        # Read Repos Configuration File
        logger.info("Loading Repos File")
        config_dict = safe_load(file)

        # Verify Empty Repos Configuration File
        if config_dict is None:
            logger.error(EmptyReposFileError())
            raise EmptyReposFileError

        # Validate Repos Configuration File
        repos_validation, err = validate_repos(config_dict=config_dict)
        if err:
            logger.error("Unvalid Repos File")
            raise err

    # Fetch Repos Data
    for provider in config_dict.keys():
        if provider == "github":
            logger.info("Fetching Github Data")
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
            logger.info("Fetching Gitlab Data")
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

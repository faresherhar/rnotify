from yaml import safe_load
import logging

from utils.validator.repos import validate_repos
from database import SessionLocal, engine
from config import settings
from exc import EmptyReposFileError
import logging_config

from utils.providers.github import get_github_latest_release
from cruds.github import add_github_release
from models.github import Github

from utils.providers.gitlab import get_gitlab_latest_release
from cruds.gitlab import add_gitlab_release
from models.gitlab import Gitlab


# Create DB Session
def get_db_session():
    db_session = SessionLocal()
    try:
        return db_session
    except:
        db_session.close()


# Define logger
logger = logging.getLogger(__name__)

# Create Tables [IF NOT EXISTS]
logger.info("Initiating Tables Creation")
Github.metadata.create_all(bind=engine)
Gitlab.metadata.create_all(bind=engine)


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
logger.info("Fetching Repos Data")
for provider in config_dict.keys():
    if provider == "github":
        logger.info("Adding Github Data")
        for repo_name in config_dict["github"]:
            release_body = get_github_latest_release(repo_name)
            if release_body:
                add_github_release(
                    repo_name=repo_name,
                    release_id=release_body["id"],
                    release_body=release_body,
                    db_session=get_db_session(),
                )
    if provider == "gitlab":
        logger.info("Adding Gitlab Data")
        for repo_name in config_dict["gitlab"]:
            release_body = get_gitlab_latest_release(repo_name)
            if release_body:
                add_gitlab_release(
                    repo_name=repo_name,
                    tag_name=release_body["tag_name"],
                    release_body=release_body,
                    db_session=get_db_session(),
                )

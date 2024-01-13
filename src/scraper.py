from yaml import safe_load

from utils.validator.repos import validate_repos
from database import SessionLocal, engine
from exc import EmptyConfigError

from utils.providers.github import get_github_latest_release
from cruds.github import add_github_release
from models.github import Github

from utils.providers.gitlab import get_gitlab_latest_release
from cruds.gitlab import add_gitlab_release
from models.gitlab import Gitlab


# Create Tables [IF NOT EXISTS]
Github.metadata.create_all(bind=engine)
Gitlab.metadata.create_all(bind=engine)


# Create DB Session
def get_db_session():
    db_session = SessionLocal()
    try:
        return db_session
    except:
        db_session.close()


# Load Repos Configuration
with open("samples/repos/good_repos.yaml", "r") as file:
    # Read Repos Configuration File
    config_dict = safe_load(file)

    # Verify Empty Repos Configuration File
    if config_dict is None:
        raise EmptyConfigError

    # Validate Repos Configuration File
    repos_validation = validate_repos(config_dict=config_dict)
    if repos_validation[0] is False:
        raise repos_validation[1]

# Fetch Repos Data
for provider in config_dict.keys():
    if provider == "github":
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
        for repo_name in config_dict["gitlab"]:
            release_body = get_gitlab_latest_release(repo_name)
            if release_body:
                add_gitlab_release(
                    repo_name=repo_name,
                    tag_name=release_body["tag_name"],
                    release_body=release_body,
                    db_session=get_db_session(),
                )

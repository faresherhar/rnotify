# from utils.repos.github import get_latest_release

# from database import SessionLocal, engine
# from models.github import Github
# from cruds.github import add_release

# Github.metadata.create_all(bind=engine)


# def get_db():
#     db = SessionLocal()
#     try:
#         return db
#     except:
#         db.close()


from yaml import safe_load

from utils.repos_validator import validate_repos
from exc import EmptyConfigError


with open("samples/bad_repos.yaml", "r") as file:
	config_dict = safe_load(file)
	if config_dict is None:
		raise EmptyConfigError	

	repos_validation = validate_repos(config_dict=config_dict)
	if repos_validation[0] is False:
		raise repos_validation[1]

	github_config = config_dict['github']

for repo in github_config:
	print(repo)



# repo_name = "grafana/grafana"
# release_body = get_latest_release(repo_name)

# add_release(
#     repo_name=repo_name,
#     release_id=release_body["id"],
#     release_body=release_body,
#     db_session=get_db(),
# )

from providers.github import get_latest_release

from database import SessionLocal, engine
from models.github import Github
from cruds.github import add_release, get_release
from providers.github import get_latest_release


Github.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        return db
    except:
        db.close()


repo_name = "grafana/grafana"
release_body = get_latest_release(repo_name)


# add_release(
#     repo_name=repo_name,
#     release_id=release_body["id"],
#     release_body=release_body,
#     db_session=get_db(),
# )

# release = get_release(
#     repo_name=repo_name,
#     release_id=134462902,
#     db_session=get_db(),
# )

# print(release)

print(type(get_latest_release(repo_name=repo_name)))

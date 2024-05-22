from database import engine, get_db_session

from cruds.repo import add_repo

from models.release import Release
from models.repo import Repo


Release.metadata.create_all(bind=engine)
Repo.metadata.create_all(bind=engine)


repo_data = [
    {"provider": "github", "owner": "grafana", "repo": "grafana"},
    {"provider": "github", "owner": "prometheus", "repo": "prometheus"},
    {"provider": "github", "owner": "derailed", "repo": "k9s"},
    {"provider": "gitlab", "owner": "AuroraOSS", "repo": "AuroraStore"},
]

for row in repo_data:
    add_repo(**row, db_session=get_db_session())

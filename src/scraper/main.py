# from scraper.providers.github.github import get_latest_release
# import json

from database import SessionLocal, engine
from models.github import Github

Github.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.close()


# get_db()
# print(json.dumps(get_latest_release("grafana/grafana")))

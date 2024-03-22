from fastapi import FastAPI

from cruds.repo import get_releases, get_all_releases, get_unnotified_releases
from database import SessionLocal, engine
import utils.logging_config
import logging


# Create DB session
def get_db_session():
    db_session = SessionLocal()
    try:
        logger.info("Establishing database connection")
        return db_session
    except:
        logger.error("Unable to connect to database")
        db_session.close()


# Define logger
logger = logging.getLogger(__name__)

app = FastAPI()


@app.get("/releases")
async def list_all_releases():
    return get_all_releases(db_session=get_db_session())


@app.get("/releases/unnotified")
async def list_unnotified_releases():
    return get_unnotified_releases(db_session=get_db_session())


@app.get("/releases/{provider}")
async def list_releases(provider: str):
    return get_releases(provider=provider, db_session=get_db_session())

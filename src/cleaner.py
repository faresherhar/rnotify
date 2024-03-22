import logging

from database import SessionLocal, engine
import utils.logging_config

from cruds.repo import delete_notified_release
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

    # Remove notified releases
    logger.info("Cleaning...")
    delete_notified_release(db_session=get_db_session())

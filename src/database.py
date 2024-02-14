from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
import logging

from config import settings
import utils.logging_config as logging_config


# Define logger
logger = logging.getLogger(__name__)

# Connect to DBMS
try:
    logger.info("Establishing databse connection")
    engine = create_engine(settings.DATABASE_URI)
except SQLAlchemyError:
    logger.error("Unable to connect to datasase")
    raise SQLAlchemyError

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

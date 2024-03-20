from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import logging

from config import settings
import utils.logging_config as logging_config


# Define logger
logger = logging.getLogger(__name__)

# Connect to DBMS
engine = create_engine(settings.DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

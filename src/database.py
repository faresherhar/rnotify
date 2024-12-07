from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import settings


# Create DB session
def get_db_session():
    db_session = SessionLocal()
    try:
        return db_session
    except:
        db_session.close()


# Connect to DB
engine = create_engine(settings.database_uri, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import settings


engine = create_engine(settings.DATABASE_URI)
SessionLocal = sessionmaker(auto_commit=False, auto_flash=False, bind=engine)

Base = declarative_base()

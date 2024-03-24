from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Repo(Base):
    __tablename__ = "repo"

    provider = Column(String(255), nullable=False, primary_key=True)
    repo_name = Column(String(255), nullable=False, primary_key=True)
    tag_name = Column(String(255), nullable=False, primary_key=True)
    notified = Column(Boolean, nullable=False, primary_key=True)

    def as_dict(self):
        return {
            "provider": self.provider,
            "repo_name": self.repo_name,
            "tag_name": self.tag_name,
            "notified": self.notified,
        }

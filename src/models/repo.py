from sqlalchemy import Column, String
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    ...


class Repo(Base):
    __tablename__ = "repo"

    provider = Column(String, nullable=False, primary_key=True)
    owner = Column(String, nullable=False, primary_key=True)
    repo = Column(String, nullable=False, primary_key=True)


    def as_dict(self):
        return {"provider": self.provider, "owner": self.owner, "repo": self.repo}

from sqlalchemy import Column, String

from models.base import Base


class Repo(Base):
    __tablename__ = "repo"

    provider = Column(String, nullable=False, primary_key=True)
    owner = Column(String, nullable=False, primary_key=True)
    repo = Column(String, nullable=False, primary_key=True)


    def as_dict(self):
        return {"provider": self.provider, "owner": self.owner, "repo": self.repo}

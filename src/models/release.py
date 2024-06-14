from sqlalchemy import Column, String, Boolean
from pydantic import BaseModel

from models.base import Base


class Release(Base):
    __tablename__ = "release"

    provider = Column(String, nullable=False, primary_key=True)
    owner = Column(String, nullable=False, primary_key=True)
    repo = Column(String, nullable=False, primary_key=True)
    tag = Column(String, nullable=False, primary_key=True)
    notified = Column(Boolean, nullable=False)

    def as_dict(self):
        return {
            "provider": self.provider,
            "owner": self.owner,
            "repo": self.repo,
            "tag": self.tag,
            "notified": self.notified,
        }


class ReleaseSchema(BaseModel):
    provider: str
    owner: str
    repo: str
    tag: str
    notified: bool

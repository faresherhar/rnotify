from sqlalchemy import Column, String, Boolean, Text
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    ...


class Release(Base):
    __tablename__ = "release"

    provider = Column(String, nullable=False, primary_key=True)
    owner = Column(String, nullable=False, primary_key=True)
    repo = Column(String, nullable=False, primary_key=True)
    tag = Column(String, nullable=False, primary_key=True)
    changelog = Column(Text, nullable=False)
    notified = Column(Boolean, nullable=False)


    def as_dict(self):
        return {"provider": self.provider, "owner": self.owner, "repo": self.repo, "tag": self.tag, "changelog": self.changelog, "notified": self.notified}

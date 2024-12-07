from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, String


class Base(DeclarativeBase): ...


class Release(Base):
    __tablename__ = "release"

    provider = Column(String, nullable=False, primary_key=True)
    repo_name = Column(String, nullable=False, primary_key=True)
    tag_name = Column(String, nullable=False, primary_key=True)
    release_url = Column(String, nullable=False, primary_key=False)

    def as_dict(self):
        return {
            "provider": self.provider,
            "repo_name": self.repo_name,
            "tag_name": self.tag_name,
            "release_url": self.release_url,
        }

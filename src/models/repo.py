from sqlalchemy import Column, String, JSON, Boolean

from database import Base


class Repo(Base):
    __tablename__ = "repo"

    provider = Column(String(255), nullable=False, primary_key=True)
    repo_name = Column(String(255), nullable=False, primary_key=True)
    tag_name = Column(String(255), nullable=False, primary_key=True)
    release_body = Column(JSON, nullable=False)
    notified = Column(Boolean, nullable=False)

    def as_dict(self):
        return {
            "provider": self.provider,
            "repo_name": self.repo_name,
            "tag_name": self.tag_name,
            "release_body": self.release_body,
            "notified": self.notified,
        }

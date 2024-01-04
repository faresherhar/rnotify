from sqlalchemy import Column, String, Integer, JSON, Boolean

from database import Base


class Github(Base):
    __tablename__ = "github"

    repo_name = Column(String(50), nullable=False, primary_key=True)
    release_id = Column(Integer, nullable=False, primary_key=True)
    release_body = Column(JSON, nullable=False)
    notified = Column(Boolean, nullable=False)

    def as_dict(self):
        return {
            "provider": self.__tablename__,
            "repo_name": self.repo_name,
            "release_id": self.release_id,
            "release_body": self.release_body,
            "notified": self.notified,
        }

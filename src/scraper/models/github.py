from sqlalchemy import Column, String, Integer, JSON

from database import Base


class Github(Base):
    __tablename__ = "github"

    repo_name = Column(String(50), nullable=False, primary_key=True)
    release_id = Column(Integer, nullable=False, primary_key=True)
    release_body = Column(JSON, nullable=False)

    def __init__(
        self,
        repo_name: str,
        release_id: int,
        release_body: dict[str, str | dict[str, str]],
    ):
        self.repo_name = repo_name
        self.release_id = release_id
        self.release_body = release_body

from sqlalchemy import Column, String
from pydantic import BaseModel

from models.base import Base


class Slack(Base):
    __tablename__ = "slack"

    webhook_token = Column(String, nullable=False, primary_key=True)

    def as_dict(self):
        return {"webhook_token": self.webhook_token}


class SlackSchema(BaseModel):
    webhook_token: str

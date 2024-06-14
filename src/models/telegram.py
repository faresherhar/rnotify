from sqlalchemy import Column, String
from pydantic import BaseModel

from models.base import Base


class Telegram(Base):
    __tablename__ = "telegram"
    
    bot_token = Column(String, nullable=False, primary_key=True)
    chat_id = Column(String, nullable=False, primary_key=True)


    def as_dict(self):
        return {"bot_token": self.bot_token, "chat_id": self.chat_id}


class TelegramSchema(BaseModel):
    bot_token: str
    chat_id: str

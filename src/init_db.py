if __name__ == "__main__":
    from database import engine
    from models.base import Base
    from models.repo import Repo
    from models.release import Release
    from models.platform.telegram import Telegram
    from models.platform.slack import Slack

    Base.metadata.create_all(bind=engine)

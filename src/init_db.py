if __name__ == "__main__":
    from database import engine
    from models.base import Base
    from models.repo import Repo
    from models.release import Release
    

    Base.metadata.create_all(bind=engine)

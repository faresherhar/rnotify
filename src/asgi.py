from fastapi import FastAPI

from database import engine
from models.release import Release
from models.repo import Repo
from routers import release
from routers import repo


app = FastAPI()

app.include_router(release.router)
app.include_router(repo.router)

Release.metadata.create_all(bind=engine)
Repo.metadata.create_all(bind=engine)

from fastapi import FastAPI
from .routes import main_router

app = FastAPI(
    title = "Groot",
    version = "0.1.0",
    descrtption="Groot is a posting app",
)

app.include_router(main_router)

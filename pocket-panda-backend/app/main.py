from fastapi import FastAPI
from app.routers import auth

app = FastAPI(title="Pocket Panda API")

app.include_router(auth.router)

# Import and include routers here (placeholders live in app/routers)
# from .routers import example
# app.include_router(example.router)

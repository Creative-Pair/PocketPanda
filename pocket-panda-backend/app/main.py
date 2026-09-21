from fastapi import FastAPI
from app.routers import auth, accounts, categories, goals, transactions, assets

app = FastAPI(title="Pocket Panda API")

app.include_router(auth.router)
app.include_router(accounts.router)
app.include_router(categories.router)
app.include_router(goals.router)
app.include_router(transactions.router)
app.include_router(assets.router)

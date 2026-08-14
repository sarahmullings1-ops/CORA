from fastapi import FastAPI
from config import APP_ENV
from api.routes.webhooks import router as webhook_router
#from contextlib import asynccontextmanager

# UNCOMMENT WHEN ALL THE APIs ARE ADDED
# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     missing = []
#     if not OPENAI_API_KEY:
#         missing.append("OPENAI_API_KEY")
#     if not DATABASE_URL:
#         missing.append("DATABASE_URL")
#     if missing:
#         print(f"WARNING: Missing env vars: {', '.join(missing)}")

#     yield

#     missing.clear

app = FastAPI(
    title="CORA",
    description="AI agent backend for contractor clients",
    version="0.1.0",
    docs_url="/docs" if APP_ENV == "development" else None
    #lifespan=lifespan // UNCOMMENT WHEN APIs ARE ADDED
)

@app.get("/health")
async def health_check():
    return {"status": "ok", "env": APP_ENV}

app.include_router(webhook_router)

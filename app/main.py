from fastapi import FastAPI
from app.api.api_v1.endpoints.routers import router as notification_router


app = FastAPI()
app.include_router(router=notification_router, prefix="")

import uvicorn
from fastapi import FastAPI
from fastapi.routing import APIRouter
from .api import password_router


app = FastAPI(title="Password API", version="1.0.0")

main_api_router = APIRouter()

main_api_router.include_router(password_router, tags=["password"])
app.include_router(main_api_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

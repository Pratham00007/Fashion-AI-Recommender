from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.upload import router as upload_router
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI(
    title="Fashion AI API",
    version="1.0.0"
)
PROJECT_ROOT = Path(__file__).resolve().parent.parent

IMAGE_FOLDER = PROJECT_ROOT / "dataset" / "fashion-dataset" / "images"

app.mount(
    "/images",
    StaticFiles(directory=str(IMAGE_FOLDER)),
    name="images"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload_router)


@app.get("/")
def home():
    return {
        "message": "Fashion AI Backend Running 🚀"
    }
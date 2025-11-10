from fastapi import FastAPI
from src.presentation.api.routes import router

app = FastAPI(title="GeoNames API", version="1.0")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "GeoNames API is running"}

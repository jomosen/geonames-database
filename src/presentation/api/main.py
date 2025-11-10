from fastapi import FastAPI
from src.presentation.api import routes

app = FastAPI(title="GeoNames API", version="1.0", debug=True)

app.include_router(routes.router)

@app.get("/")
def root():
    return {"message": "GeoNames API is running"}

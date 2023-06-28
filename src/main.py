import uvicorn
from fastapi import FastAPI

from src.api.endpoints import products as products_endpoint

app: FastAPI = FastAPI(title="Inventory API")
app.include_router(products_endpoint.router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)

from fastapi import APIRouter

from src.services.product_service import ProductService

router: APIRouter = APIRouter(prefix="/products", tags=["Products"])
product_service: ProductService = ProductService()

@router.get("/")
async def get_all_products():
    return await product_service.get_all_products()

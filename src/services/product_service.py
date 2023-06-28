from src.models.product import Product

class ProductService:
    def __init__(self):
        self.model = Product

    async def get_all_products(self) -> list[str]:
        return self.model.all_pks()

from redis_om import HashModel

from src.core.database import redis_connection


class Product(HashModel):
    name: str
    price: float
    quantity: int

    class Meta:
        database = redis_connection

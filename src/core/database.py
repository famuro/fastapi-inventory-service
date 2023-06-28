from redis import Redis
from redis_om import get_redis_connection

from src.utils import config

settings: config.Settings = config.get_settings()

redis_connection: Redis = get_redis_connection(
    host=settings.db_host,
    port=settings.db_port
)



from redis import asyncio as aioredis
from core import Config

redis = aioredis.from_url(Config.REDIS_URL, decode_responses=True)

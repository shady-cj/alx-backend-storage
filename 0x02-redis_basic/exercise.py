#!/usr/bin/env python3
"""
 The module contains a Cache class. In the __init__ method, store an
 instance of the Redis client as a private variable
 named _redis (using redis.Redis()) and flush the instance using flushdb.
"""
import redis
import uuid
import typing


class Cache:
    """
    Stores a value into the redis store
    """
    def __init__(self) -> None:
        """
        initialize redis connection
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: typing.Union[str, bytes, int, float]) -> str:
        """
        set key value for each call to store
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

#!/usr/bin/env python3
"""
 The module contains a Cache class. In the __init__ method, store an
 instance of the Redis client as a private variable
 named _redis (using redis.Redis()) and flush the instance using flushdb.
 basically to implement a caching system
"""
import redis
import uuid
import typing
from functools import wraps


def count_calls(method: typing.Callable) -> typing.Callable:
    """
    A decorator that takes in a method and increment
    the number of times it's called
    """
    @wraps(method)
    def count(self, *args):
        """
        counts and returns the original methods
        """
        meth = method.__qualname__
        if self._redis.get(meth) is None:
            self._redis.set(meth, 1)
        else:
            self._redis.incr(meth)
        return method(self, *args)
    return count


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

    @count_calls
    def store(self, data: typing.Union[str, bytes, int, float]) -> str:
        """
        set key value for each call to store
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: typing.Optional[typing.Callable[[],
            any]] = None):
        """
        get the key and return the correct type
        """
        value = self._redis.get(key)
        if fn is None:
            return value
        return fn(value)

    def get_str(self, key: str) -> typing.Union[str, None]:
        """
        get the key and return a str
        """
        return self.get(key, str)

    def get_int(self, key: str) -> typing.Union[int, None]:
        """
        get the key and return an int
        """
        return self.get(key, int)

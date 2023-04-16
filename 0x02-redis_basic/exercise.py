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


def call_history(method: typing.Callable) -> typing.Callable:
    """
    A decorator that stores a methods input and output results
    """
    @wraps(method)
    def exec_append(self, *args):
        """
        appends the inputs parameter to the input list
        """
        meth_input_name = f"{method.__qualname__}:inputs"
        meth_output_name = f"{method.__qualname__}:outputs"
        self._redis.rpush(meth_input_name, str(args))
        output = method(self, *args)
        self._redis.rpush(meth_output_name, output)
        return output
    return exec_append


def replay(method: typing.Callable):
    """
    show the history of the method call
    """
    meth_name = method.__qualname__
    r_instance = redis.Redis()
    length = r_instance.llen(f"{meth_name}:inputs")
    input_lists = r_instance.lrange(f"{meth_name}:inputs", 0, -1)
    output_lists = r_instance.lrange(f"{meth_name}:outputs", 0, -1)
    print(f"{meth_name} was called {length} times:")
    zipped_in_out = list(zip(input_lists, output_lists))
    for in_, out in zipped_in_out:
        print(f"{meth_name}(*{in_.decode('utf-8')})\
 -> {out.decode('utf-8')}")


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
    @call_history
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

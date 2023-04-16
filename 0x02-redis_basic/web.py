#!/usr/bin/env python3
"""
implementing a get_page
function (prototype: def get_page(url: str) -> str:)
"""
import requests
import redis
import typing
import functools



def count_url(fn: typing.Callable) -> typing.Callable:
    """
    decorator to get the number of times url was used in
    get_page
    """
    @functools.wraps(fn)
    def count(url):
        red = redis.Redis()
        red.flushdb()
        if red.exists(f"count:{url}"):
            red.incr(f"count:{url}")
        else:
            red.setex(f"count:{url}", 10, 1)
        return fn(url)
    return count


@count_url
def get_page(url: str) -> str:
    """
    getting the page and caching the url for 10 seconds
    """
    ret = requests.get(url)
    return ret.content

# get_page('https://www.google.com')
# get_page('https://www.google.com')
# get_page('https://www.google.com')
# print(red.get("count:https://www.google.com"))
# import time
# time.sleep(10)
# get_page('https://www.google.com')
# get_page('https://www.google.com')
# print(red.get("count:https://www.google.com"))

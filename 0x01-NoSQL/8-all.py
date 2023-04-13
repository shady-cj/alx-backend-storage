#!/usr/bin/python3
"""
This module contains a Python function that lists all documents in a collection:
"""


def list_all(mongo_collections):
    """
    Listing all the documents present in mongo_collection using pymongo
    """
    return mongo_collections.find()
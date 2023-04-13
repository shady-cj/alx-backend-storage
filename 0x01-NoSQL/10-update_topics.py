#!/usr/bin/env python3
"""
A Python function that changes all topics of a school document based
on the name:
"""


def update_topics(mongo_collection, name, topics):
    """
    updates the mongo_collection with the name of arg name and an
    attribute topics
    """

    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})

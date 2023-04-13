#!/usr/bin/env python3
"""
The module contains a Python function that returns the list of school
having a specific topic:
"""


def schools_by_topic(mongo_collection, topic):
    """
    return schools that has the topic in their list of
    topics
    """

    return mongo_collection.find({"topics": topic})
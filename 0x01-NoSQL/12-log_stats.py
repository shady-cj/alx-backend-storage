#!/usr/bin/env python3
"""
a Python script that provides some stats about Nginx logs stored in MongoDB:
"""
from pymongo import import MongoClient


def main():
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx = client.logs.nginx
    x_logs = nginx.find().count()
    aggregate_logs = nginx.aggregate([{"$group": {"method": "$method", "num_of_occurence": {"$sum": 1}}}])

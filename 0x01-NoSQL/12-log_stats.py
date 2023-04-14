#!/usr/bin/env python3
"""
a Python script that provides some stats about Nginx logs stored in MongoDB:
"""
from pymongo import MongoClient


def main():
    """
    prints the stats from the nginx logs
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx = client.logs.nginx
    x_logs = nginx.count_documents({})
    aggregate_logs = nginx.aggregate([{"$group": {"_id": "$method", "num_of_occurence": {"$sum": 1}}}])
    methods = {}
    for m in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        for m_log in aggregate_logs:
            if m == m_log.get('_id'):
                methods[m] = m_log.get('num_of_occurence')
                break
        if methods.get(m):
            continue
        methods[m] = 0

    print(f"{x_logs} logs")
    print("Methods:")
    for meth in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        print(f"    method {meth}: {methods.get(meth)}")
    stat_check = nginx.count_documents({"method": "GET", "path": "/status"})
    print(f"{stat_check} status check")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
a Python function that returns all students sorted by average score:
"""


def top_students(mongo_collection):
    """
    Using aggregation to find the average score of student
    """
    collection = mongo_collection.aggregate(
        [
            {"$unwind": "$topics"},
            {"$group":
                {
                    "_id": "$name",
                    "id": {"$first": "$_id"},
                    "name": {"$first": "$name"},
                    "averageScore": {"$avg": "$topics.score"}
                }
             },
            {"$sort": {"averageScore": -1}},
            {"$project": {
                            "_id": "$id",
                            "name": "$name",
                            "averageScore": "$averageScore"
                        }
             }
        ])
    return collection

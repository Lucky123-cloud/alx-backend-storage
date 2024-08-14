#!/usr/bin/env python3


"""
Write a Python function that returns the list of school having a specific topic:

Prototype: def schools_by_topic(mongo_collection, topic):
mongo_collection will be the pymongo collection object
topic (string) will be topic searched
"""


def schools_by_topic(mongo_collection, topic):
	"""
	This function has to return list of schools having a specific topic
	"""
	return mongo_collection.find({ "topic": topic })

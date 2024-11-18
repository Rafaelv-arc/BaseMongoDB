from inserirnomongo import collection

pipeline = [
    {"$match": {"idade": {"$gte": 30}}},
    {"$group": {"_id": "$cidade", "media_idade": {"$avg": "$idade"}}}
]
result = collection.aggregate(pipeline)
for doc in result:
    print(doc)

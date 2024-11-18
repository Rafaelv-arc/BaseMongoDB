from inserirnomongo import collection, client


with client.start_session() as session:
    with session.start_transaction():
        collection.update_one({"nome": "Maria"}, {"$set": {"idade": 31}}, session=session)
        collection.insert_one({"nome": "Pedro", "idade": 28}, session=session)

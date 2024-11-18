from inserirnomongo import collection

# Atualizar um único documento
collection.update_one({"nome": "João"}, {"$set": {"idade": 26}})

# Atualizar vários documentos
collection.update_many({"cidade": "Rio de Janeiro"}, {"$set": {"estado": "RJ"}})

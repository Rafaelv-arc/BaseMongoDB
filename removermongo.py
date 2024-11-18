from inserirnomongo import collection

# Atualizar um único documento
collection.delete_one({"nome": "João"})

# Atualizar vários documentos
collection.delete_many({"cidade": "Rio de Janeiro"})

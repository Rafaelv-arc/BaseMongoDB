from inserirnomongo import collection

# aqui é apenas uma consulta especifica
resultado = collection.find_one({"nome": "João"})
print(resultado)


# Buscar todos os documentos usamos for in para percorrer tudo

for doc in collection.find():
    print(doc)
    
    
# filtrar documentos com condições ( misturamos ambas as consultas de unico e todos)

for doc in collection.find({"idade": {"$gt": 25}}):
    print(doc)
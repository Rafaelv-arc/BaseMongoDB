from inserirnomongo import collection

#Cria um index em um campo específico
collection.create_index("nome")

#Cria um índice composto
collection.create_index([("nome", 1), ("idade", 1)])
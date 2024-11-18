from pymongo import MongoClient
from pymongo.errors import ConnectionError, OperationFailure

try:
    client = MongoClient("mongodb://localhost:27017/", maxPoolSize=50, minPoolSize=5)
    db = client['TesteAutoBD']
    print("Conexão bem-sucedida!")
except ConnectionError as e:
    print(f"Erro de conexão: {e}")
except OperationFailure as e:
    print(f"Erro na operação: {e}")

collection = db['systemteste'] # coleções são como tabelas em um banco de dados relacional(no caso o MongoDB é NOSQL por isso e variavel a estrutura em JSON)

documento = {"nome": "João", "idade": 25, "cidade": "São Paulo"}
result = collection.insert_one(documento) # aqui é inserido os dados

print(f"ID do documento inserido: {result.__inserted_id}") # mostrando o registro da afirmação que foi registrado com sucesso no banco de dados



# Inserir vários documentos
documentos = [
    {"nome": "Maria", "idade": 30, "cidade": "Rio de Janeiro"},
    {"nome": "Carlos", "idade": 35, "cidade": "Belo Horizonte"}
]
result = collection.insert_many(documentos)
print(f"IDs dos documentos inseridos: {result.inserted_ids}")
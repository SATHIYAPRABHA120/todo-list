# import pymongo
# import certifi

# client = pymongo.MongoClient(
#     "mongodb+srv://sathiyaprabha012:Vinayagarrr%407@cluster0.is1woh5.mongodb.net/",
#     tls=True,
#     tlsCAFile=certifi.where()
# )

# try:
#     print("Databases:", client.list_database_names())
# except Exception as e:
#     print("Error:", e)
import pymongo
import certifi

client = pymongo.MongoClient(
    "mongodb+srv://sathiyaprabha012:Vinayagarrr%407@cluster0.is1woh5.mongodb.net/",
    tls=True,
    tlsCAFile=certifi.where()
)

try:
    print(client.list_database_names())
except Exception as e:
    print("Error:", e)

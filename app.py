from azure.cosmos import CosmosClient

URL ="https://foodie.documents.azure.com:443/"
KEY ="nZOBrQ5E6HYWVmVj1kJZju574JiWtezEET8VpgZQOIQP1AUO80IswbG2c2EWFBlPvJUUfYsEceRo7QirmCc1rw=="
client = CosmosClient(URL, credential=KEY)

database_name = 'testDatabase'
try:
    database = client.create_database(database_name)
except exceptions.CosmosResourceExistsError:
    database = client.get_database_client(database_name)

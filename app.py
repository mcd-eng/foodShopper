import os
from dotenv import load_dotenv
from azure.cosmos import CosmosClient

URL = os.getenv("URL")
KEY = os.getenv("KEY")
client = CosmosClient(URL, credential=KEY)

database_name = 'testDatabase'
try:
    database = client.create_database(database_name)
except exceptions.CosmosResourceExistsError:
    database = client.get_database_client(database_name)

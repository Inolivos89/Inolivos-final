
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv
load_dotenv()

class Mongo:
    def __int__(self):
        user = os.getenv("MONGO-USER")
        password = os.getenv("MONGO-PASS")
        host = os.getenv("MONGO-HOST")
        uri = f"mongodb+srv://{user}:{password}@{host}/?retryWrites=true&w=majority"

        # Create a new client and connect to the server
        self.client = MongoClient(uri, server_api=ServerApi('1'))

    def test_connection(self):

        # Send a ping to confirm a successful connection
        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)
if __name__ == "__main__":
    Mongo().test_connection()
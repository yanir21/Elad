import pymongo
from bson.json_util import dumps

def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb://elad:Qh3QYbnabuBUiANAlzFdl02Y2xUqVBZffZretLZDAUVRkA6IJhbYfkGcK6DUe1GOTqZD0AHSN6AcotifgHDB0Q==@elad.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@elad@"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = pymongo.MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['elad']
    
def get_collection():
        # Get the database
    dbname = get_database()
    # Create a new collection
    collection_name = dbname["OptionTree"]

    collection = collection_name.find()
    final = []

    for item in collection:
        final.append(item)

    return (final)

#if __name__ == "__main__":    
#   print(get_collection())

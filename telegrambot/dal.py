def get_database():
    from pymongo import MongoClient
    import pymongo

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb://elad:Qh3QYbnabuBUiANAlzFdl02Y2xUqVBZffZretLZDAUVRkA6IJhbYfkGcK6DUe1GOTqZD0AHSN6AcotifgHDB0Q==@elad.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@elad@"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['elad']
    
def get_collection():
        # Get the database
    dbname = get_database()
    # Create a new collection
    collection_name = dbname["OptionTree"]

    tree = collection_name.find()
    return tree
    
if __name__ == "__main__":    
    

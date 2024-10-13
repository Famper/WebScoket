from pymongo import MongoClient
from pymongo.results import InsertOneResult

# Provide the mongodb atlas url to connect python to mongodb using pymongo
CONNECTION_STRING = "mongodb://localhost:27017/"
# Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
client = MongoClient(CONNECTION_STRING)


def get_databases() -> list[str]:
    """
    Метод получения доступных БД

    :return:
    """
    # Create the database for our example (we will use the same database throughout the tutorial
    return client.list_database_names()


def create_collection() -> InsertOneResult:
    """
    Метод проверки заполнения тестовыми данными

    :return:
    """
    test_db = client['test_db']
    test_collection = test_db['test_collection']
    test_data = {"name": "test", "login": "test", "password": "<PASSWORD>"}

    return test_collection.insert_one(test_data)


# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":
    # Get the database
    print(get_databases())
    print(create_collection())



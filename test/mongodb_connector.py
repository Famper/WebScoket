from pymongo import MongoClient, version, has_c
from pymongo.results import InsertOneResult

# Provide the mongodb atlas url to connect python to mongodb using pymongo
CONNECTION_STRING = "mongodb://localhost:27017/"
# Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
client = MongoClient(CONNECTION_STRING)


def get_data() -> dict[str, bool]:
    """
    Метод получения данных исходя из установленного пакета

    :return: dict[str, bool]
    """
    return {"version": version, "has_c": bool(has_c)}


def get_databases() -> list[str]:
    """
    Метод получения доступных БД

    :return: list[str]
    """
    # Create the database for our example (we will use the same database throughout the tutorial
    return client.list_database_names()


def create_collection() -> InsertOneResult:
    """
    Метод проверки заполнения тестовыми данными

    :return: pymongo.results.InsertOneResult
    """
    test_db = client['test_db']
    test_collection = test_db['test_collection']
    test_data = {"name": "test", "login": "test", "password": "<PASSWORD>"}

    return test_collection.insert_one(test_data)


# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":
    print(get_data())

    # Get the database
    print(get_databases())
    print(create_collection())



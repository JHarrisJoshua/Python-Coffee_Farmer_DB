import os
from dotenv import load_dotenv, find_dotenv
import psycopg2
import psycopg2.extras

# Load environment variables from the .env file
load_dotenv(find_dotenv())

# Set the database URL (Heroku URL from config)
DATABASE_URL = os.environ.get("DATABASE_URL")
#user = os.environ.get("USER")
#passwd = os.environ.get("PW")
#db = os.environ.get("DB")

def connect_to_database():
    """
    connects to the database
    """
    db_connection = psycopg2.connect(DATABASE_URL, sslmode='require')
    return db_connection

def execute_query(db_connection = None, query = None, query_params = ()):
    """
    executes a given SQL query on the given db connection and returns a Cursor object
    db_connection: connection object created by connect_to_database()
    query: SQL query
    returns: A Cursor object
    """

    if db_connection is None:
        print("No connection to the database found")
        return None

    if query is None or len(query.strip()) == 0:
        print("Query is empty")
        return None

    print("Executing %s with %s" % (query, query_params))

    # Create a cursor to execute query.
    cursor = db_connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cursor.execute(query, query_params)
    db_connection.commit()
    return cursor


if __name__ == '__main__':
    print("Executing a sample query on the database")
    db = connect_to_database()
    query = "SELECT * from Varieties;"
    results = execute_query(db, query)
    print("Printing results of %s" % query)

    for r in results.fetchall():
        print(r)

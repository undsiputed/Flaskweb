import mysql.connector
from mysql.connector import Error

def create_connection():
    """
    Create a database connection.
    Update the host, database, user, and password with your MySQL credentials.
    """
    try:
        connection = mysql.connector.connect(
            host='sql5.freesqldatabase.com',  # Replace with your database host
            database='sql5755219',  # Replace with your database name
            user='sql5755219',  # Replace with your MySQL username
            password='d1sdlZvdcI'  # Replace with your MySQL password
        )
        if connection.is_connected():
            print("Successfully connected to the database")
            return connection
    except Error as e:
        print(f"Error: '{e}' occurred while connecting to the database")
        return None

def execute_query(connection, query):
    """
    Execute a single query.
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"Error: '{e}' occurred while executing the query")

def fetch_results(connection, query):
    """
    Fetch results from the database.
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    except Error as e:
        print(f"Error: '{e}' occurred while fetching results")
        return []

if __name__ == "__main__":
    # Create a database connection
    conn = create_connection()

    if conn:
        # Example: Fetch data from jobs table
        select_query = "SELECT * FROM jobs;"
        jobs = fetch_results(conn, select_query)

        # Display the fetched jobs
        for job in jobs:
            print(job)

        # Close the connection
        conn.close()

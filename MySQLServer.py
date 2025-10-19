import mysql.connector

def create_alx_book_store_db():
 
    DB_CONFIG = {
        'host': 'localhost',
        'user': 'mysql',  
        'password': '123456789' 
    }

    db_connection = None
    db_cursor = None

    try:
        
        db_connection = mysql.connector.connect(**DB_CONFIG)
        db_cursor = db_connection.cursor()

        CREATE_DB_QUERY = "CREATE DATABASE IF NOT EXISTS alx_book_store"

        db_cursor.execute(CREATE_DB_QUERY)

        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:

        print(f"Error: Failed to connect to the DB or execute query.")
        print(f"MySQL Error details: {err}")

    finally:
        if db_cursor:
            db_cursor.close()
        if db_connection and db_connection.is_connected():
            db_connection.close()
            print("DB connection closed.")

if __name__ == "__main__":
    create_alx_book_store_db()

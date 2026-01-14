"""
Python and Database Access

Python can be used to connect to and interact with a wide variety of databases.
The Python standard for database interfaces is the Python DB-API (PEP 249).
Most Python database interfaces adhere to this standard.

This file contains notes on accessing various databases with Python.
"""

# ==============================================================================
# Supported Databases
# ==============================================================================

# Python supports a vast range of database systems, including but not limited to:
# - GadFly
# - MySQL
# - PostgreSQL
# - Microsoft SQL Server
# - Informix
# - Oracle
# - Sybase
# - SQLite
# - and many more...

# ==============================================================================
# Python DB-API
# ==============================================================================

# The Python DB-API provides a standard interface for working with databases.
# The general workflow involves:
# 1. Importing the appropriate database adapter module.
# 2. Creating a connection object to the database.
# 3. Creating a cursor object from the connection.
# 4. Executing SQL queries using the cursor object.
# 5. Fetching the results of the query.
# 6. Closing the cursor and the connection.

# A cursor object is a control structure that enables traversal over the records in a database.
# Cursors facilitate subsequent processing in conjunction with the traversal, such as retrieval,
# addition, and removal of database records.

# ==============================================================================
# Common Database Packages/Adapters
# ==============================================================================

# To connect to a specific database, you typically need to install a third-party library (adapter).
# Here are some common adapters for popular databases:

# Oracle:
#   - cx_Oracle (pip install cx_Oracle)
#   - pyodbc (pip install pyodbc)

# Microsoft SQL Server:
#   - pymssql (pip install pymssql)
#   - pyodbc (pip install pyodbc)

# PostgreSQL:
#   - psycopg2 (pip install psycopg2-binary)

# MySQL:
#   - MySQL Connector/Python (pip install mysql-connector-python)
#   - PyMySQL (pip install PyMySQL)


# ==============================================================================
# Example: Using SQLite (Built-in)
# ==============================================================================

# SQLite is a C library that provides a lightweight disk-based database that doesn’t
# require a separate server process and allows accessing the database using a nonstandard
# variant of the SQL query language. The `sqlite3` module is included with Python.

import sqlite3

def sqlite_example():
    """
    A simple example demonstrating the DB-API using the built-in sqlite3 module.
    """
    # 1. Create a connection object.
    # This will create a file named 'example.db' if it doesn't exist.
    try:
        conn = sqlite3.connect('example.db')
        print("Successfully connected to the database.")

        # 2. Create a cursor object.
        cursor = conn.cursor()

        # 3. Execute SQL queries.
        # Create a table (if it doesn't exist)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            )
        ''')
        print("Table 'users' created or already exists.")

        # Insert some data
        try:
            cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ('Alice', 'alice@example.com'))
            cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ('Bob', 'bob@example.com'))
            print("Inserted sample data.")
        except sqlite3.IntegrityError:
            print("Sample data already exists.") # Avoids error on re-run

        # Commit the changes to the database
        conn.commit()

        # 4. Execute a SELECT query to fetch data.
        print("\nFetching user data:")
        cursor.execute("SELECT id, name, email FROM users")

        # 5. Fetch the results.
        # fetchone() - retrieves the next row of a query result set
        # fetchall() - fetches all (remaining) rows of a query result
        # fetchmany(size) - retrieves the next set of rows of a query result
        all_users = cursor.fetchall()
        for user in all_users:
            print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}")

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        # 6. Close the connection.
        # The cursor is automatically closed when the connection is closed.
        if 'conn' in locals() and conn:
            conn.close()
            print("\nDatabase connection closed.")

if __name__ == '__main__':
    sqlite_example()

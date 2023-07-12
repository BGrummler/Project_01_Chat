import sqlite3
from sqlite3 import Error
from pathlib import Path

    """
    Checks if the provided username and password are valid for login.

    :param username: The username entered by the user.
    :param password: The password entered by the user.
    :return: True if the login is successful, False otherwise.
    """
def user_login(username, password):

    # Set up the path to the database file
    current_path = Path.cwd()
    database =  current_path /"test.db"

    def create_connection(db_file):
        """Creates a database connection to the SQLite database specified by db_file.

        :param db_file: The path to the SQLite database file.
        :return: Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print("connection")
            return conn
        except Error as e:
            print(e)

        return conn
    
    def select_table(table, column='*', where=''):
        """
        Executes a SELECT query on the specified table with optional columns and WHERE clause.

        :param table: The name of the table to query.
        :param column: The columns to select (default is '*').
        :param where: The WHERE clause for filtering (default is an empty string).
        :return: The fetched rows from the table.
        """
        try:
            cursor = connection.cursor()
            select_table_sql = f"SELECT {column} FROM {table} {where};"
            cursor.execute(select_table_sql)
            return cursor.fetchall()
        except Error as e:
            print(e)
    
    # Create a connection to the database

    connection = create_connection(database)
    
    sql_return = select_table('User', 'Nickname, Password', f"WHERE Nickname = '{username}'")
    value = len(sql_return) > 0 and sql_return[0][0] == username and sql_return[0][1] == password

    connection.close()

    return value
import sqlite3
from sqlite3 import Error
from pathlib import Path

# Set up the path to the database file
current_path = Path.cwd()
database = str(current_path / "test.db")


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


def user_login(username, password):
    """
    Checks if the provided username and password are valid for login.

    :param username: The username entered by the user.
    :param password: The password entered by the user.
    :return: True if the login is successful, False otherwise.
    """
    
    sql_return = select_table('User', 'Nickname, Password', f"WHERE Nickname = '{username}'")
    print(sql_return)
    return len(sql_return) > 0 and sql_return[0][0] == username and sql_return[0][1] == password


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

# Prompt for username and password with a maximum of three attempts
# for _ in range(3):
#     print('Please Enter')
#     input_username = input('Username: ')
#     input_password = input('Password: ')

#     if user_login(input_username, input_password):
#         print('Welcome ' + input_username)
#         break
#     else:
#         print('Try again')
# else:
#     print("Wrong input, Shutdown")
#     connection.close()
#     quit()


# # Print the user table
# print("\n" + 70 * "_" + "\n\n" + 25 * " " + "USER TABLE\n" + 70 * "_" + "\n")  # Fat Line
# sql_return = select_table('User')  # Fetching the whole table
# for row in sql_return:
#     print(row)

#connection.close()

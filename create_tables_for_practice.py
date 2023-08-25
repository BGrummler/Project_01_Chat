import sqlite3
from sqlite3 import Error
from pathlib import Path

current_path = Path.cwd()
server_db = str((current_path) / "server_database.db")
client_db = str((current_path) / "client_database.db")

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print()

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def create_tables():


    sql_create_user_table = """CREATE TABLE IF NOT EXISTS USER (
                                    ChatID INTEGER PRIMARY KEY AUTOINCREMENT,
                                    Nickname VARCHAR(32),
                                    Password VARCHAR(32),
                                    Private BOOL DEFAULT FALSE
                                );"""

    sql_create_server_chat_table = """CREATE TABLE IF NOT EXISTS SERVER_CHAT (
                                        ChatID INTEGER PRIMARY KEY AUTOINCREMENT,
                                        Date TIMESTAMP,
                                        SourceUserID VARCHAR(32),
                                        TargetUserID VARCHAR(32),
                                        Message VARCHAR(500)
                                    );"""

    sql_create_client_chat_table = """CREATE TABLE IF NOT EXISTS CLIENT_CHAT (
                                        ChatID INTEGER PRIMARY KEY AUTOINCREMENT,
                                        SOURCE_ID INTEGER,
                                        Date TIMESTAMP,
                                        SourceUserID VARCHAR(32),
                                        TargetUserID VARCHAR(32),
                                        Message VARCHAR(500)
                                    );"""
    
    sql_create_client_friendlist = """CREATE TABLE IF NOT EXISTS CLIENT_FRIENDLIST (
                                        FriendUserID VARCHAR(32),
                                        Source_UserID VARCHAR(32)
                                    );"""


    # create a database connection
    conn = create_connection(server_db)


    # create user table
    create_table(conn, sql_create_user_table)

    # create singlechat table
    create_table(conn, sql_create_server_chat_table)

    print("Server DB Created")
    
    
    conn = create_connection(client_db)

    # create groupchat table
    create_table(conn, sql_create_client_chat_table)
    create_table(conn, sql_create_client_friendlist)

    print("Local DB Created")



create_tables()
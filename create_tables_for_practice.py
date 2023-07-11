import sqlite3
from sqlite3 import Error
from pathlib import Path

current_path = Path.cwd()
database = str((current_path) / "test.db") #"try" to fix path-issue

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


def main():
    # database = r"C:\FIAE\Python\Project1Chat\test.db"

    sql_create_logins_table = """CREATE TABLE IF NOT EXISTS LOGINS (
                                    LoginID INTEGER PRIMARY KEY AUTOINCREMENT,
                                    UserNick VARCHAR(32) NOT NULL,
                                    Date DATETIME DEFAULT CURRENT_TIMESTAMP
                                );"""

    sql_create_user_table = """CREATE TABLE IF NOT EXISTS USER (
                                    Nickname VARCHAR(32) PRIMARY KEY,
                                    Password VARCHAR(32),
                                    Read BIGINT DEFAULT 0
                                );"""

    sql_create_singlechat_table = """CREATE TABLE IF NOT EXISTS SINGLECHAT (
                                        SingleChatID INTEGER PRIMARY KEY AUTOINCREMENT,
                                        SourceUserID INTEGER,
                                        TargetUserID INTEGER,
                                        SingleMassage VARCHAR(500),
                                        FOREIGN KEY (SourceUserID) REFERENCES USER (UserID),
                                        FOREIGN KEY (TargetUserID) REFERENCES USER (UserID)
                                    );"""

    sql_create_groupchat_table = """CREATE TABLE IF NOT EXISTS GROUPCHAT (
                                        GroupchatID INTEGER PRIMARY KEY AUTOINCREMENT,
                                        SourceUserID INTEGER,
                                        Groupname VARCHAR(32),
                                        GroupMassage VARCHAR(500)
                                    );"""

    sql_create_authorisation_table = """CREATE TABLE IF NOT EXISTS AUTHORISATION (
                                            AuthorisationID INTEGER PRIMARY KEY AUTOINCREMENT,
                                            UserID INTEGER,
                                            SingleChatID INTEGER,
                                            GroupChatID INTEGER,
                                            FOREIGN KEY (UserID) REFERENCES USER (UserID),
                                            FOREIGN KEY (SingleChatID) REFERENCES SINGLECHAT (SingleChatID),
                                            FOREIGN KEY (GroupChatID) REFERENCES GROUPCHAT (GroupChatID)
                                        );"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create logins table
        create_table(conn, sql_create_logins_table)

        # create user table
        create_table(conn, sql_create_user_table)

        # create singlechat table
        create_table(conn, sql_create_singlechat_table)

        # create groupchat table
        create_table(conn, sql_create_groupchat_table)

        # create authorisation table
        create_table(conn, sql_create_authorisation_table)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()

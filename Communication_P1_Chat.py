import sqlite3
from sqlite3 import Error
from pathlib import Path

current_path = Path.cwd()
database_path = current_path/"test.db"


# this list isnt used at all i keep it for database reference
tables_p1_chat = {
    "server": {
        "server.user": ["Nickname PK", "Message.MessageID FK", "Password", "pending", "Private_Mode", "Hidden_Mode"],
        "server.group": ["Group_Name PK","admins fk"],
        "server.permissions": ["permissions_id", "user.nickname fk" "target usergroup fk"],
        "server.usergroup": ["UserGroup_ID", "User.Nickname FK", "Group.Groupname FK"],
        "server.message": ["Message_ID PK", "Message_From FK", "Message_To FK", "Message_Body"],
    },
    "client": {
        "client.chats": ["server.group.Group_Name FK","server.user.Nickname FK" ],
        "client.message": ["Message_ID PK FK", "Message_From FK", "Message_To FK", "Message_Body TK"] #Temp Key
    },
}


#i have not decided if i want to put the queries into each function or have the functions reference this list yet...
sql_queries = {
    "insert_user": "INSERT INTO User (Nickname, Password) VALUES (?, ?)",
    "select_user_by_nickname": "SELECT * FROM User WHERE Nickname = ?",
    "login" : "SELECT Nickname, Password FROM User WHERE Nickname = ?" #'User', 'Nickname, Password', f"WHERE Nickname = '{username}'")
        # Add other queries as needed
}

def try_except(function): 
    """
    decorator function to handle all try → except logic and the cursor

    Arguments:
        function: function to wrap
        c: sqlite3.cursor
    
    Returns:
        wrapped function
    """
    def wrapper(*args, **kwargs):
        global conn
        try:
            c = conn.cursor()
            return function(c, *args, **kwargs)
        except Error as e:
            print(f"Error in {function.__name__}: {e}")
    return wrapper


def create_connection(db_file:str) -> sqlite3.Connection:
    """ 
    creates a database connection to the SQLite databas specified by db_file

    Arguments:
        db_file path to database

    Returns: 
        Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn


@try_except
def create_account(c:sqlite3.Cursor, new_user:str, new_password:str):
    """
    create new account on the database

    Arguments:
        c: sqlite 3 cursor object
        new_user: Nickname for the new user
        password: password for the new user

    Returns:
        None
    """
    insert_query = "INSERT INTO User (Nickname, Password) VALUES (?, ?)"            
    c.execute(insert_query, (new_user, new_password))
    conn.commit()


@try_except
def does_nickname_exist(c:sqlite3.Cursor, nickname:str) -> tuple:
    """
    checks if the username already exists

    Arguments:
        c: cursor for database communication
        nickname: nickname to seach for in the database

    Returns:
        Tuple with the nickname if any, else empty tuple
    """
    select_query = "SELECT * FROM User WHERE Nickname = ?"
    c.execute(select_query, (nickname,))
    return c.fetchone()


@try_except
def select_users(c:sqlite3.Cursor) -> list[tuple]:
    """
    TODO
    """
    select_query = "SELECT * FROM User"
    c.execute(select_query)
    return c.fetchall()


@try_except
def select_table(c, table, column = '*', WHERE = ''):
    """
    #outdated
    """
    select_table_sql = f"SELECT {column} FROM {table} {WHERE};"
    c.execute(select_table_sql)
    return c.fetchall()


@try_except
def filter_results_by_WHERE(table, new_user): 
    """
    #outdated

    If needed overwrite the default WHERE = '' with WHERE = filter_results_by_WHERE in the select_table() FUNKTION 
    """
    where_string_sql = f"WHERE {table} = '{new_user}'"
    return where_string_sql


@try_except
def user_login(c:sqlite3.Cursor, nickname:str, password:str):
    """
    compare entered username and password witht he database

    Arguments:
        c: cursor for database communication
        nickname: input from user
        password: input from user

    Returns:
        bool: True if user exists and corresponding password is correct 
    """
    select_query = "SELECT Nickname, Password FROM User WHERE Nickname = ?"
    c.execute(select_query, (nickname,))
    check_name_pw = c.fetchone()
    return check_name_pw != None and check_name_pw[0] == nickname and check_name_pw[1] == password



def send_Message():
    pass

def get_Message():
    pass

def delete_Message():
    pass

def join_Group():
    pass

def invite_Friend():
    pass

def close_connection():
    conn.close()

conn = create_connection(database_path)

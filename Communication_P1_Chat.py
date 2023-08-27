import sqlite3
from sqlite3 import Error
from pathlib import Path


current_path = Path.cwd()
server_path = current_path/"server_database.db"
client_path = current_path/"client_database.db"

# this list isnt used att all i keep it for database reference
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
        global conn_server
        global conn_client
        try:
            cursor_server = conn_server.cursor()
            cursor_client = conn_client.cursor()
            c = (cursor_server, cursor_client)
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
def user_login(c:tuple[sqlite3.Cursor,sqlite3.Cursor], nickname:str, password:str):
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
    c[0].execute(select_query, [nickname])
    check_name_pw = c[0].fetchone()
    return check_name_pw != None and check_name_pw[0] == nickname and check_name_pw[1] == password


@try_except
def create_account(c:tuple[sqlite3.Cursor,sqlite3.Cursor], new_user:str, new_password:str):
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
    c[0].execute(insert_query, [new_user, new_password])
    conn_server.commit()


@try_except
def nickname_exist(c:tuple[sqlite3.Cursor,sqlite3.Cursor], nickname:str) -> tuple:
    """
    checks if the username already exists
    Arguments:
        c: cursor for database communication
        nickname: nickname to seach for in the database
    Returns:
        Tuple with the nickname if any, else empty tuple
    """
    select_query = "SELECT * FROM User WHERE Nickname = ?"
    c[0].execute(select_query, [nickname])
    return c[0].fetchone()


@try_except
def select_user(c:tuple[sqlite3.Cursor,sqlite3.Cursor]) -> list[tuple]:
    """
    TODO
    """
    select_query = "SELECT * FROM User"
    c[0].execute(select_query)
    return c[0].fetchall()

@try_except
def select_friend(c:tuple[sqlite3.Cursor,sqlite3.Cursor], source_nick:str) -> list[tuple]:
    """
    TODO
    """
    select_query = "SELECT FriendUserID FROM CLIENT_FRIENDLIST WHERE Source_UserID = ?"
    c[1].execute(select_query, [source_nick])
    return c[1].fetchall()

@try_except
def delete_Account(c:tuple[sqlite3.Cursor,sqlite3.Cursor], nickname):
    delete_query = "DELETE FROM User WHERE Nickname = ?"
    c[0].execute(delete_query, [nickname])
    conn_server.commit()
    delete_query = "DELETE FROM CLIENT_FRIENDLIST WHERE Nickname = ?"
    c[1].execute(delete_query, [nickname])
    conn_client.commit()


@try_except
def add_Friend(c:tuple[sqlite3.Cursor,sqlite3.Cursor], target:str, source:str) -> None:
    """
    add a account on the local database
    Arguments:
        c: sqlite 3 cursor object
        nickname: user to add to the locan database
    Returns:
        None
    """
    insert_query = "INSERT INTO CLIENT_FRIENDLIST (FriendUserID, Source_UserID) VALUES (?, ?)"
    c[1].execute(insert_query, [target, source])
    conn_client.commit()


@try_except
def send_Message(c:tuple[sqlite3.Cursor,sqlite3.Cursor],date, source, destination, message):
    insert_query = "INSERT INTO SERVER_CHAT (Date, SourceUserID, TargetUserID, Message) VALUES (?, ?, ?, ?)"            
    c[0].execute(insert_query, [date, source, destination, message])
    c[0].connection.commit()

#TODO
@try_except
def save_Message(c:tuple[sqlite3.Cursor,sqlite3.Cursor],id, date, source, destination, message):
    insert_query = "INSERT INTO CLIENT_CHAT (SOURCE_ID, Date, SourceUserID, TargetUserID, Message) VALUES (?, ?, ?, ?, ?)"           
    c[1].execute(insert_query, [id, date, source, destination, message])
    c[1].connection.commit()


@try_except
def get_Message(c:tuple[sqlite3.Cursor,sqlite3.Cursor], source_nick:str) -> list[tuple]:
    """
    TODO
    """
    select_query = "SELECT * FROM SERVER_CHAT WHERE TargetUserID = ?"
    c[0].execute(select_query, [source_nick])
    return c[0].fetchall()


@try_except
def delete_Message(c:tuple[sqlite3.Cursor,sqlite3.Cursor], source):
    delete_query = "DELETE FROM SERVER_CHAT WHERE ChatID = ?"
    c[0].execute(delete_query, [source])
    conn_server.commit()


def join_Group():
    pass


@try_except
def delete_all(c:tuple[sqlite3.Cursor,sqlite3.Cursor]) -> None:
    """
    TRUNCATES ALL DATA FROM SERVER AND CLIENT !!!WARNING!!!
    """
    delete_query = "DELETE FROM USER"
    c[0].execute(delete_query)
    delete_query = "DELETE FROM SERVER_CHAT"
    c[0].execute(delete_query)
    c[0].connection.commit()
    delete_query = "DELETE FROM CLIENT_CHAT"
    c[1].execute(delete_query)
    delete_query = "DELETE FROM CLIENT_FRIENDLIST"
    c[1].execute(delete_query)
    c[1].connection.commit()

def close_connection():
    conn_client.close()
    conn_server.close()

conn_server = create_connection(server_path)
conn_client = create_connection(client_path)

import sqlite3
from sqlite3 import Error
from pathlib import Path

current_path = Path.cwd()
database = str((current_path) / "test.db")
#database = r"C:\FIAE\Python\Project1Chat\test.db" # TODO adjust appopriaty, maybe we can make this address calculated by current folder ?

def create_connection(db_file):
    """ 
    creates a database connection to the SQLite databas specified by db_file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_account(new_user, new_password):
    try:
        c = conn.cursor()
        new_account_sql = f"INSERT INTO User (Nickname, Password) VALUES ('{new_user}','{new_password}');"
        c.execute(new_account_sql)
        conn.commit()
        new_user_confirmation = select_table('user', 'Nickname',filter_results_by_WHERE('Nickname',new_user))[0][0] # checks for the new entry
        print("New User "+ new_user_confirmation + " created") 
    except Error as e:
        print(e)

def select_table(table, column = '*', WHERE = ''): # default column is * | default WHERE statement is '' = empty
    try:
        c = conn.cursor()
        select_table_sql = f"SELECT {column} FROM {table} {WHERE};"
        #print(select_table_sql)
        c.execute(select_table_sql)
        return c.fetchall()
    except Error as e:
        print(e)

def filter_results_by_WHERE(table, new_user): #If needed overwrite the default WHERE = '' with WHERE = filter_results_by_WHERE in the sselect_table() FUNKTION 
    where_string_sql = f"WHERE {table} = '{new_user}'"
    return where_string_sql

conn = create_connection(database)
new_user = input('Username: ')
new_password = input('Password: ')
create_account(new_user,new_password)
print("\n" + 70 * "_"  + "\n\n"+ 25 * " " + "USER TABLE\n" + 70 * "_"+"\n") # Fat Line
sql_return = select_table('User') # Printing the whole table
for elem in sql_return:
    print(elem)
conn.close()

# Terminal for P1_Chat
import Communication_P1_Chat as CPC

language = 1
nickname = None


def print_menu(menu_dict:dict, language:int) -> str:
    """
    function to print the menu options of functions according to theyr nested keys in a dictionary

    Arguments:
        dict_command_local: dictionary with functions and descriptions:strings
        menu_dict: function.__name__ passed from the wrapper so the function knows what key to print
        language: integer stored in a variable to choose wich language to index in the dictionary

    Prints the Menu options of the current function
    """
    print("\nMenu\n")
    for key,elem in dict_command_local[menu_dict].items():
        print(key, elem[language])


def handle_name(target_function):
    """
    decorator to handle function names and errors
    calls the print_menu

    Arguments: 
        target_function - the function that gets wrapped
        target_function.__name__ as parameter to the menu_print function
    
    returns the wrapped function
    """
    def wrapper(*args, **kwargs):
        f_name = target_function.__name__
        print_menu(f_name, language)
        try: return target_function(*args, **kwargs)
        except KeyError: print(f"Error in {f_name}")
    return wrapper


@handle_name
def Greet_P1_Chat():
    """
    Initial screen displays options:    
    returns function chosen by corresponding input
    """
    while True:
        _i = input()
        try: return dict_command_local["Greet_P1_Chat"][_i][0]()
        except KeyError: print("Wrong Input Line 29")


def Login_P1_Chat():
    """
    Login function → checks for correct username and password
    returns main chat window and username
    """
    print("\nLogin\n")
    for _ in range(3):
        nickname = input("Please enter your Nickname: ")
        password = input("Please enter your Password: ")
        if CPC.user_login(nickname, password): return Main_P1_Chat(nickname)
        else: print("Wrong Input Line 38")
    print("Wrong Input loging out"), quit()


@handle_name
def Options_P1_Chat():
    """
    TODO
    """
    print("Options not implemented yet")
    Greet_P1_Chat()
    _ = input(">>> ")


def Create_Account_P1_Chat():
    """
    Checks if User already exists if != 
    Creates new entries in the user database

    returns to the Login Screen
    """
    while True:
        print('Enter "B" for back')
        new_name = input("Please Enter new Nickname: ")
        if str.lower(new_name) == "b": return Greet_P1_Chat() # b for back to Login Screen
        if CPC.does_nickname_exist(new_name) == None: break
        else: print("Nickname " + new_name + " unavailable")
    new_password = input("Please Enter new Password: ")
    CPC.create_account(new_name, new_password)
    print("new User " + CPC.does_nickname_exist(new_name)[0] + " created")
    return Greet_P1_Chat()


@handle_name
def Main_P1_Chat(username=None):
    """
    Main Chat Window with options to chat or invite
    returns function accordingly
    """
    print(f"Welcome {username}")
    _ = input(">>> ")
    dict_command_local["Main_P1_Chat"][_][0]()


@handle_name
def select_chatroom(username=None):
    """
    Select Group or Person to chat with
    """
    print(f"Welcome {username}")
    _ = input(">>> ")
    dict_command_local["select_chatroom"][_][0]()


def Quit_P1_Chat():
    """
    closes the cursor
    quits the programm
    """
    CPC.close_connection()
    quit()


def invite_friend():
    pass


def join_group():
    pass


def Send_Message_P1_Chat():
    pass



def  Delete_Message_P1_Chat():
    pass



def Join_Group_P1_Chat():
    pass



def Invite_P1_Chat():
    pass



def Logout_P1_Chat():
    Greet_P1_Chat()

#dictionary with functions and descriptions
dict_command_local = {
    "Greet_P1_Chat": {
        "1": [Login_P1_Chat, "Login", "Einloggen"],
        "2": [Create_Account_P1_Chat, "Create Account", "Account anlegen"],
        "3": [Options_P1_Chat, "Options", ""],
        "0": [Quit_P1_Chat, "Quit", "Beenden"]
    },
    "Options_P1_Chat": { #placeholders
        "1": [Quit_P1_Chat, "Quit", "Beenden"],
        "2": [Quit_P1_Chat, "Quit", "Beenden"],
        "3": [Quit_P1_Chat, "Quit", "Beenden"],
        "4": [Quit_P1_Chat, "Quit", "Beenden"],
        "9": [Quit_P1_Chat, "Quit", "Beenden"],
        "0": [Quit_P1_Chat, "Quit", "Beenden"]
    },
    "Main_P1_Chat": {
        "1": [select_chatroom, "Select Chat", "Chat auswählen"],
        "2": [invite_friend, "Invite Friend", "Freunde einladen"],
        "2": [join_group, "Join Group", "Gruppe beitreten"],
        "9": [Logout_P1_Chat, "Logout", "Ausloggen"],
        "0": [Quit_P1_Chat, "Quit", "Beenden"]
    },
    "select_chatroom": {
        "1": [Send_Message_P1_Chat, "Send Message", "Nachricht senden"],
        "2": [Delete_Message_P1_Chat, "Delete Message", "Nachricht löschen"],
        "8": [Main_P1_Chat, "Main menu", "Hauptmenue"],
        "9": [Logout_P1_Chat, "Logout", "Ausloggen"],
        "0": [Quit_P1_Chat, "Quit", "Beenden"]
    }    
}


Greet_P1_Chat()
CPC.close_connection()
quit()

# Terminal for P1_Chat
import Communication_P1_Chat as CPC

language = 1
nickname = None


def print_menu(menu_dict:dict, language:list) -> str:
    """
    function to print the menu options of functions according to theyr nested keys in a dictionary

    Arguments:
        dict_command_local: dictionary with functions and descriptions:strings
        menu_dict: function.__name__ passed from the wrapper so the function knows what key to print
        language: integer stored in a variable to choose wich language to index in the dictionary

    Prints the Menu options of the current function
    """
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
        print("┏" + (len(f_name) + 2) * "━" + "┓")
        print("┃", f_name, "┃")
        print("┗" + (len(f_name) + 2) * "━" + "┛")
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
        _i = input(">>> ")
        return dict_command_local["Greet_P1_Chat"][_i][0]()


def Login_P1_Chat():
    """
    Login function → checks for correct username and password
    returns main chat window and username
    """
    print("┏" + 7 * "━" + "┓")
    print("┃", "Login", "┃")
    print("┗" + 7 * "━" + "┛")
    for _ in range(3):
        global nickname
        nickname = input("Please enter your Nickname: ")
        password = input("Please enter your Password: ")
        if CPC.user_login(nickname, password): return Main_P1_Chat()
        else: print("Input not correct")
    print("Wrong Input logging out"), quit()


@handle_name
def Options_P1_Chat():
    """
    Select options to change language, Terminal Colour, Private Mode

    returns: 
        function for desired option
    """
    _ = input(">>> ")
    return dict_command_local["Options_P1_Chat"][_][0]()


def Create_Account_P1_Chat():
    """
    Checks if User already exists if != 
    Creates new entries in the user database

    returns: 
        Login Screen
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


def delete_account_P1_Chat():
    """
    Deletes the Account currently logged in

    TODO
    """
    global nickname
    print("Delete account")
    while True:
        n_ = input("Press \"b\" for abort\nplease enter nickname to delete: ")
        if str.lower(n_) == "b": return Options_P1_Chat()
        if n_ == nickname: break #TODO implement password logic for confirmation
        else: print("wrong nickname") 
    


@handle_name
def Main_P1_Chat():
    """
    Main Chat Window with options to chat or invite
    returns function accordingly
    """
    global nickname
    print(f"Welcome {nickname}")
    _ = input(">>> ")
    dict_command_local["Main_P1_Chat"][_][0]()


@handle_name
def select_chatroom():
    """
    Select Group or Person to chat with
    """
    global nickname
    print(f"Welcome {nickname}")
    _ = input(">>> ")
    dict_command_local["select_chatroom"][_][0]()


def Quit_P1_Chat():
    """
    closes the connection
    quits the programm
    """
    CPC.close_connection()
    quit()


def invite_friend():
    """
    Prints all Members if Profile is not hidden and are not the current user.
    TODO implement Friendslist DB for local and implement logic to not print members already
    in the Friendslist.

    returns:
        TODO adds Member or Group to the local Database for communication
    """
    user_list = CPC.select_users()
    user_list = [elem[0] for elem in user_list if elem[2] == 0 and elem[0] != nickname] 
    # TODO add current friend DB to logic
    for i in range(len(user_list)):            
            print(user_list[i],end = (15-len(user_list[i]))*" ")
            if (i + 1) % 5 == 0: print()
    friend_invite = input("\nPlease Enter Nickname for Friend request\n>>> ")
    # TODO add Friend to Local DB
    del user_list
    pass


def select_language_P1_Chat():
    """
    Prints available Language Packs
    Changes Language
    """
    print("┏" + 10 * "━" + "┓")
    print("┃", "Language", "┃")
    print("┗" + 10 * "━" + "┛")
    print("1 english\n2 german")
    l_ = int(input(">>> "))
    if 0 < l_ < 3:
        global language
        language = l_


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
        "3": [Options_P1_Chat, "Options", "Optionen"],
        "0": [Quit_P1_Chat, "Quit", "Beenden"]
    },
    "Options_P1_Chat": {
        "1": [select_language_P1_Chat, "language", "Sprache"],
        "2": [delete_account_P1_Chat, "delete account", "Account löschen"],
        "3": [Quit_P1_Chat, "Quit", "Beenden"],
        "4": [Quit_P1_Chat, "Quit", "Beenden"],
        "9": [Quit_P1_Chat, "Quit", "Beenden"],
        "0": [Quit_P1_Chat, "Quit", "Beenden"]
    },
    "Main_P1_Chat": {
        "1": [select_chatroom, "Select Chat", "Chat auswählen"],
        "2": [invite_friend, "Invite Friend", "Freunde einladen"],
        "3": [join_group, "Join Group", "Gruppe beitreten"],
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


while True:
    if nickname != None:
        Main_P1_Chat()
    else:
        Greet_P1_Chat()

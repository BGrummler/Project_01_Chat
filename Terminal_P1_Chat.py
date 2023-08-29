# Terminal for P1_Chat
import Communication_P1_Chat as CPC
from datetime import datetime

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

    Arguments:
        username : str 

    returns:
        main chat window 
    """
    print("┏" + 7 * "━" + "┓")
    print("┃", "Login", "┃")
    print("┗" + 7 * "━" + "┛")
    for _ in range(3):
        global nickname
        nickname = None
        print("q to quit")
        nickname = input("Please enter your Nickname: ")
        if nickname == "q":
            Quit_P1_Chat()
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
        if CPC.nickname_exist(new_name) == None: break
        else: print("Nickname " + new_name + " unavailable")
    new_password = input("Please Enter new Password: ")
    CPC.create_account(new_name, new_password)
    print("new User " + CPC.nickname_exist(new_name)[1] + " created")
    CPC.add_Friend("admin", new_name)
    CPC.add_Friend(new_name, new_name)
    return Greet_P1_Chat()


def delete_account_P1_Chat():
    """
    Checks for Name and Password
    Deletes an Account

    """
    print("Delete account")
    while True:
        n_ = input("Press \"b\" for abort\nplease enter nickname to delete: ")
        if str.lower(n_) == "b": return Options_P1_Chat()
        password = input("please confirm password: ")
        if CPC.user_login(n_, password):
            CPC.delete_Account(n_)
            return Options_P1_Chat()
        else: print("wrong credentials")

    

@handle_name
def Main_P1_Chat():
    """
    Main Chat Window with options to chat or invite
    returns function accordingly
    """
    global nickname
    check_invites()
    print(f"Welcome {nickname}")
    _ = input(">>> ")
    return dict_command_local["Main_P1_Chat"][_][0]()


def check_invites():
    """
    Checks for invites from other Users on the server Database
    """
    new_messages = CPC.get_Message(nickname)
    #print(f"You have {len(new_messages)} new Messages")
    #[print(elem) for elem in new_messages]
    for elem in new_messages:
        CPC.save_Message(elem[0],elem[1], elem[2], elem[3], elem[4])
        CPC.delete_Message(elem[0])




#@handle_name
def select_chatroom():
    """
    Select Group or Person to chat with
    """
    global nickname
    print(f"Select Chat target")
    friend_list = CPC.select_friend(nickname)
    friend_list = [elem[0] for elem in friend_list]
    for i in range(len(friend_list)):
            print(i,")",friend_list[i],end = (15-len(friend_list[i]))*" ")
            if (i + 1) % 5 == 0: print()
    print("\nq for quit")
    chat_with = input(">>> ")
    if chat_with == "q":
            Quit_P1_Chat()
    elif chat_with == "0":
        new_invites = CPC.get_Message2(nickname, friend_list[int(chat_with)])
        if len(new_invites) == 0:
            print("No new Invites")
            Main_P1_Chat()
        
        lists_of_invites = [elem[4][20:] for elem in new_invites]
        [print(str(i)+")", lists_of_invites[i]) for i in range(len(lists_of_invites))]
        friend_add = input("Select Friend to Add\n>>>")
        if friend_add.isdigit() and int(friend_add) in range(len(lists_of_invites)):
            CPC.add_Friend(lists_of_invites[int(friend_add)], nickname)
            print(lists_of_invites[int(friend_add)], "added to Friends list")
            print("ID ", new_invites[int(friend_add)][0], " DELETED")
            CPC.delete_Message2(new_invites[int(friend_add)][0])
    elif chat_with.isdigit() and int(chat_with) in range(1,len(friend_list)):
        #chat_with = int(chat_with)
        return Start_Chat( friend_list[int(chat_with)])
    else: print("wrong input")



def Start_Chat(chat_with):
    chat_history = CPC.get_Message2(chat_with, nickname)
    print(50 * "_")
    print(f"Chatting with {chat_with}")
    print(50 * "_")
    [print(elem[4]) for elem in chat_history]
    print("b for back")
    message = input(">>>")
    if str.lower(message) == "b":return Main_P1_Chat()
    CPC.send_Message(datetime.now(), chat_with, nickname, message)
    check_invites()
    #new_messages = CPC.get_Message(nickname)
    return Start_Chat(chat_with)
    




def Delete_All_Data():
    CPC.delete_all()
    return Greet_P1_Chat()


def Quit_P1_Chat():
    """
    closes the connections
    quits the programm
    """
    CPC.close_connection()
    quit()


def invite_friend():
    """
    Prints all Members if Profile is not hidden and are not the local friends List.
    sends invite to member server db
    adds Member to local Friend list
    """
    user_list = CPC.select_user()
    friend_list = CPC.select_friend(nickname)
    friend_list = [elem[0] for elem in friend_list]
    user_list = [elem[1] for elem in user_list if elem[3] == 0 and elem[1] not in friend_list]
    for i in range(len(user_list)):
            print(user_list[i],end = (15-len(user_list[i]))*" ")
            if (i + 1) % 5 == 0: print()
    friend_invite = input("\nPlease Enter Nickname for Friend request\n>>> ")
    if friend_invite == "q":
        Quit_P1_Chat()
    if friend_invite in user_list:
        CPC.send_Message(datetime.now(), "admin" , friend_invite, "Friend request from " + nickname)
        CPC.add_Friend(friend_invite, nickname)
    else: print("error in invite_friend")



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



def  Delete_Message_P1_Chat():
    pass



def Join_Group_P1_Chat():
    pass



def Invite_P1_Chat():
    pass



def Logout_P1_Chat():
    global nickname
    nickname = None
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
        "4": [Delete_All_Data, "Delete all Data", "Alle Daten löschen"],
        "9": [Logout_P1_Chat, "Logout", "Ausloggen"],
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
        "1": [Start_Chat, "Send Message", "Nachricht senden"],
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

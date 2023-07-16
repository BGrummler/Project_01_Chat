# Terminal for P1_Chat
import Communication_P1_Chat as CPC

language = 1


#prints the current menu from inside the function
def print_menu(menu_dict, language):
    print("\nMenu\n")
    for key,elem in dict_command_local[menu_dict].items():
        print(key, elem[language])


#decorator to handle function names and errors

def handle_name(target_function):
    def wrapper(*args, **kwargs):
        f_name = target_function.__name__
        print_menu(f_name, language)
        try: return target_function(*args, **kwargs)
        except KeyError: print(f"Error in {f_name}")
    return wrapper


@handle_name
def Greet_P1_Chat():
    while True:
        _i = input()
        try: return dict_command_local["Greet_P1_Chat"][_i][0]()
        except KeyError: print("Wrong Input")


def Login_P1_Chat():
    print("\nLogin\n")
    for _ in range(3):
        nickname = input("Please enter your Nickname: ")
        password = input("Please enter your Password: ")
        if CPC.user_login(nickname, password): return Main_P1_Chat(nickname)
        else: print("Wrong Input")
    print("Wrong Input loging out"), quit()


@handle_name
def Options_P1_Chat():
    print("Options not implemented yet")
    Main_P1_Chat()
    _ = input(">>> ")


def Create_Account_P1_Chat():
    while True:
        new_name = input("Please Enter new Nickname: ") # TODO make it possible to quit 
        print(CPC.does_nickname_exist(new_name))
        if CPC.does_nickname_exist(new_name) == None: break
        else: print("Nickname " + new_name + " unavailable")
    new_password = input("Please Enter new Password: ")
    CPC.create_account(new_name, new_password)


@handle_name
def Main_P1_Chat(Username=None):
    print(f"Welcome {Username}")
    _ = input(">>> ")
    dict_command_local["Main_P1_Chat"][_][0]()



def select_chatroom():
    pass



def Quit_P1_Chat():
    CPC.close_connection()
    quit()



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


dict_command_local = {
    "Greet_P1_Chat": {
        "1": [Login_P1_Chat, "Login", "Einloggen"],
        "2": [Create_Account_P1_Chat, "Create Account", "Account anlegen"],
        "0": [Quit_P1_Chat, "Quit", "Beenden"]
    },
    "Options_P1_Chat": {
        "1": [Quit_P1_Chat, "Quit", "Beenden"],
        "2": [Quit_P1_Chat, "Quit", "Beenden"],
        "3": [Quit_P1_Chat, "Quit", "Beenden"],
        "4": [Options_P1_Chat, "Quit", "Beenden"],
        "9": [Main_P1_Chat, "Quit", "Beenden"],
        "0": [Quit_P1_Chat, "Quit", "Beenden"]
    },
    "Main_P1_Chat": {
        "1": [Send_Message_P1_Chat, "Send Message", "Nachricht senden"],
        "2": [Delete_Message_P1_Chat, "Delete Message", "Nachricht löschen"],
        "3": [Join_Group_P1_Chat, "Join Group", "Gruppe Beitreten"],
        "4": [Invite_P1_Chat, "Invite", "Einladen"],
        "5": [Logout_P1_Chat, "Logout", "Ausloggen"],
        "0": [Quit_P1_Chat, "Quit", "Beenden"]
    }
}


Greet_P1_Chat()
CPC.close_connection()
quit()

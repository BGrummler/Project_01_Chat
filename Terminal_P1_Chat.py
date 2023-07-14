# Terminal for P1_Chat
import Communication_P1_Chat as CPC

def print_menu(menu_dict):
    print("\nMenu\n")
    for key,elem in dict_commands[menu_dict].items():
        print(key, elem.__name__.replace("P1_Chat", "").replace("_"," "))

def handle_name(target_function):
    target_function(target_function.__name__)


def Greet_P1_Chat():
    print_menu("Greet_P1_Chat")
    dict_commands["Greet_P1_Chat"][input(">>> ")]()

def Login_P1_Chat():
    print("\nplease Enter your credentials\n")
    for _ in range(3):
        nickname = input("Please enter your Nickname: ")
        password = input("Please enter your Password: ")
        if CPC.user_login(nickname, password): Main_P1_Chat(nickname)
        else: print("wrong try again")
    print("wrong input Logout")

def Options_P1_Chat():
    print("Options not implemented yet")
    Main_P1_Chat()
    _ = input(">>> ")

def Create_Account_P1_Chat():
    new_name = input("Please Enter new Nickname")
    new_password = input("Please Enter new Password")
    CPC.create_account(new_name, new_password)

def Main_P1_Chat(Username=None):
    print(f"Welcome {Username}")
    print_menu("Main_P1_Chat")
    _ = input(">>> ")
    dict_commands["Main_P1_Chat"][_]()

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

dict_commands = {
    "Greet_P1_Chat": {
        "1": Login_P1_Chat,
        "2": Create_Account_P1_Chat,
        "0": Quit_P1_Chat
    },
    "Options_P1_Chat": {
        "1": Quit_P1_Chat,
        "2": Quit_P1_Chat,
        "3": Quit_P1_Chat,
        "4": Options_P1_Chat,
        "9": Main_P1_Chat,
        "0": Quit_P1_Chat
    },
    "Main_P1_Chat": {
        "1": Send_Message_P1_Chat,
        "2": Delete_Message_P1_Chat,
        "3": Join_Group_P1_Chat,
        "4": Invite_P1_Chat,
        "5": Logout_P1_Chat,
        "0": Quit_P1_Chat
    }
}

Greet_P1_Chat()
CPC.close_connection()
Quit_P1_Chat()
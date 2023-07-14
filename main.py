from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.metrics import dp
import login_001 as lg

current_user        = None
current_user_pw     = None

class Manager(ScreenManager):
    pass

class LogInScreen(Screen):

    login_counter = 0 #to be used later for finite attempts
    
    def on_pre_enter(self):
        Window.size = (dp(350), dp(220))

    def validate_login(self):
        global current_user
        global current_user_pw     
        user_name = self.ids.user_text.ids.username.text
        user_pw   = self.ids.user_pw.ids.passwort.text
        if lg.user_login(user_name, user_pw):
            app              = App.get_running_app()
            app.root.current = "ChatScreen"
            current_user     = user_name
            current_user_pw  = user_pw
        else:
            self.ids.user_text.ids.username.text = ""
            self.ids.user_pw.ids.passwort.text   = ""

class ChatScreen(Screen):

    def on_pre_enter(self):
        Window.size = (dp(800), dp(600))
    

class RightColumn(BoxLayout):

    def testChat(self):
        left_label = self.parent.parent.ids.left_column.ids.ScrollChat.ids.left_label
        chat_input = self.parent.parent.ids.left_column.ids.chat_input

        if chat_input.text != "":
            left_label.text =  left_label.text + "\n" + chat_input.text
            chat_input.text = ""
            
class LeftColumn(BoxLayout):
    pass

class ChatProject(App):
    pass

ChatProject().run()
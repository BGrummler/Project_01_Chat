from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen



class Manager(ScreenManager):
    pass

class LogInScreen(Screen):
        
    def validate_login(self, widget):
        print("ja")
            

class ChatScreen(Screen):
    pass


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

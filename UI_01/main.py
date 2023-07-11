from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class Widgets(BoxLayout):
    pass


class RightColumn(BoxLayout):

    def testChat(self):
        left_label = self.parent.ids.left_column.ids.ScrollChat.ids.left_label
        chat_input = self.parent.ids.left_column.ids.chat_input

        if chat_input.text != "":
            left_label.text =  left_label.text + "\n" + chat_input.text
            chat_input.text = ""
            chat_input.focus = True


class LeftColumn(BoxLayout):
    pass


class ChatProject(App):
    pass


ChatProject().run()

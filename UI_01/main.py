from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget

chatSimulation = StringProperty("Hier steht dann Chat")

class Widgets(GridLayout):
    pass

  
class InfoAndButton(BoxLayout):
    chatSimulation = StringProperty("Hier steht dann Zeug\n")
    
    def testChat(self):
        self.chatSimulation = self.chatSimulation + "Und noch eine Zeile\n"

class ChatProject(App):
    pass

ChatProject().run()
import kivy
kivy.require('1.0.7')
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class MyTextInput(TextInput):
    def __init__(self, text, componentMbst=False, **kwargs):
        super(MyTextInput, self).__init__(**kwargs)
        self.componentMbst = componentMbst
        self.bind(on_text=self.update_height)
        self.height=200
        self.line_height=250
        self.text = text
    def update_height(self, instance, value):
        self.minimum_height = self.height
        
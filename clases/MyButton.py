import kivy
kivy.require('1.0.7')
from kivy.uix.button import Button

class MyButton(Button):
    def __init__(self, componentMbst=False, **kwargs):
        super(MyButton, self).__init__(**kwargs)
        self.componentMbst = componentMbst

        

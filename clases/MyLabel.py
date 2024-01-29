import kivy
kivy.require('1.0.7')
from clases.MyBoxLayout import MyBoxLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class MyLabel(Label):
    def __init__(self, text, componentMbst=False, **kwargs):
        super(MyLabel, self).__init__(**kwargs)
        
        # print("MyLabel",text)
        # self.size_hint=(1, None)
        # self.spacing=0
        # self.orientation='vertical'
        # label = Label(text=text)
        # self.add_widget(label)
        self.text = text
        self.componentMbst = componentMbst

        

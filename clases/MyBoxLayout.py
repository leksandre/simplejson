import kivy
kivy.require('1.0.7')
from kivy.uix.boxlayout import BoxLayout
class MyBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MyBoxLayout, self).__init__(**kwargs)
        self.bind(minimum_height=self.setter('height'))

    def add_widget(self, widget, index=0):
        super(MyBoxLayout, self).add_widget(widget, index)
        self.do_layout()
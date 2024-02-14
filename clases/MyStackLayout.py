import kivy
kivy.require('1.0.7')
from kivy.uix.stacklayout import StackLayout

class MyStackLayout(StackLayout):

    def add_widget(self, widget, index=0):
        super(MyStackLayout, self).add_widget(widget, index)
 
    def __init__(self, componentMbst=False, **kwargs):
        super(MyStackLayout, self).__init__(**kwargs)
        self.componentMbst = componentMbst
        self.bind(minimum_height=self.setter('height'))
        self.bind(height=self.setter('height'))
        self.bind(children=self._on_children_changed)
        # self.size_hint_y = None

    def _on_children_changed(self, instance, value):
        children = self.children
        
        # self.height = self.height + 100

        # max = 0
        # sum = 0
        # for child in children:
        #     print('MyStackLayout child.height',child.height)    
        #     if child.height>max:
        #         max = child.height
        #     sum = sum + child.height
        
        # self.height = sum 

        
        

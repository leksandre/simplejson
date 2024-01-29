import kivy
kivy.require('1.0.7')
from clases.MyBoxLayout import MyBoxLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from random import random

class MyLabel(Label):
    def __init__(self, text, componentMbst=False, **kwargs):
        super(MyLabel, self).__init__(**kwargs)
        
        
        self.text = text
        
        print("MyLabel",text,self.text_size)
        
        
        
        
        self.size_hint = (None, None)
        self.size_hint_max = (1, 1) 
        self.height=30
        # self.width=200
        # from kivy.core.window import Window
        # self.size_hint=(None, None)
        self.halign='center'
        self.valign='middle'
        self.multiline=True
        # self.spacing=10
        self.padding=(20,20)
        
        
        
        
        # self.orientation='vertical'
  
        
        
        self.set_random_background()
        
        
        # label.text_size=(None, None)
        # label.halign='center'
        # label.spacing=10
        # label.padding=(2,2)
        # label.valign='middle'
        # label.multiline=True
        

        # self.bind(size=lambda instance, value: setattr(self, 'text_size', value))
        
        
        #MyBoxLayout
        # label = Label(text=text)
        # label.text = text
        # label.height=20
        # self.add_widget(label)
        # self.text = text

        
        self.componentMbst = componentMbst

    def set_random_background(self):
        with self.canvas.before:
            # Генерация случайного цвета фона
            r, g, b = random(), random(), random()
            Color(r, g, b, mode='rgb')
            # Нарисовать фоновый прямоугольник
            self.rect = Rectangle(pos=self.pos, size=self.size)

        self.bind(pos=self.update_background, size=self.update_background)

    def update_background(self, instance, value):
        instance.rect.pos = instance.pos
        instance.rect.size = instance.size



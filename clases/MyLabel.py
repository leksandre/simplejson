import kivy
kivy.require('1.0.7')
from clases.MyBoxLayout import MyBoxLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from random import random

class MyLabel(MyBoxLayout):
    def __init__(self, text, componentMbst=False, **kwargs):
        super(MyLabel, self).__init__(**kwargs)
        self.componentMbst = componentMbst
        
        
        self.height = 40
        self.text = text
        self.bind(size=self._update_size)
        
        
        
        
        
        
        # self.multiline = True
        # self.outline_color=(1, 0, 0, 1)
        # self.outline_width=2
        # self.size_hint = (1, None)
        # self.bind(size=lambda instance, value: setattr(self, 'text_size', value))
        
        # print("MyLabel text - ",text,self.text_size)

        # self.spacing = 1 
        # self.size_hint = (None, None)
        # self.size_hint_max = (1, 1) 
        # self.height=30
        # self.halign='center'
        # self.valign='middle'
        # self.multiline=True
        # self.padding=(20,20)

        # self.set_random_background()

        # self.orientation='vertical'
        # self.spacing=10
        # self.width=200
        # from kivy.core.window import Window
        # self.size_hint=(None, None)

        # label.text_size=(None, None)
        # label.halign='center'
        # label.spacing=10
        # label.padding=(2,2)
        # label.valign='middle'
        # label.multiline=True








        #MyBoxLayout
        #AnchorLayout
        self.anchor_x='center'
        self.anchor_y='center'
        self.size_hint = (1, None)
        label = Label(text=text)
        self.add_widget(label)
        
        
        #  size_hint=(1, None),  # Отключаем автоматическую адаптацию размера по содержимому
                    #   size=(400, 100),  # Задаем фиксированный размер Label
                    #   text_size=(400, None),  # Ограничиваем ширину текста по горизонтали
                    #   halign='center',  # Выравнивание текста по центру
                    #   valign='middle'
                      
        
        # label.bind(size=lambda instance, value: setattr(label, 'text_size', value))
        # label.multiline = True
        # label.text = text
        # label.outline_color=(1, 0, 0, 1)
        # label.outline_width=2

        
        # label.size_hint = (1, None)
    
        
    def _update_size(self, instance, value):
        # self.canvas.before.clear()
        self.size_hint = (1, None)
        
        # if self.parent is not None:
        #     parent_type = type(self.parent).__name__
        #     if parent_type!="MyBoxLayout":
        #         print('Parent type:', parent_type)
        #         self.size_hint_max = self.parent.size_hint 
        # else:
        #     # self.size_hint = (1, None)
        #     # self.size_hint_max = (1, None)
        #     pass
        
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



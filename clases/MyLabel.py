import kivy
kivy.require('1.0.7')
from kivy.uix.label import Label
# from clases.MyBoxLayout import MyBoxLayout
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.anchorlayout import AnchorLayout
# from kivy.graphics import Color, Rectangle
# from kivy.uix.scrollview import ScrollView

from random import random

class MyLabel(Label):
    def __init__(self, text, componentMbst=False, **kwargs):
        super(MyLabel, self).__init__(**kwargs)
        self.componentMbst = componentMbst
        #label
        # self.bind(size=self._update_size)
        self.size_hint = (1, None)
        self.text = text
        self.height = 40
  
        text_size=(1, 1)
        self.halign='center' 
        self.valign='center'
        self.multiline = True
        self.size_hint = (1, None)
        self.bind(size=lambda instance, value: setattr(self, 'text_size', value))
        
        
        
        
        #ScrollView
        # self.height = 40
        # self.size_hint = (1, None)
        # self.anchor_x='center'
        # self.anchor_y='center'
        # # self.opacity = 0
        # self.size_hint = (1, None)
        # label = Label(text=text)
        # # label.size_hint_max = (1, None)
        # label.text_size=(None, None)
        # label.halign='center'  # Выравнивание текста по центру
        # label.valign='center'
        # # label.bind(size=lambda instance, value: setattr(self, 'text_size', value))
        # label.bind(size=lambda instance, value: setattr(self, 'text_size', value))
        # self.add_widget(label)
        
        
  
        #AnchorLayout
        #MyBoxLayout
        # self.size_hint = (1, None)
        # self.height = 40
        # # self.orientation='vertical'
        # self.bind(size=self._update_size)
        # label = Label(text=text,
        #               size_hint=(1, None),  
        #               height=50,  
        #               text_size=(None, None),  
        #               halign='left', 
        #               valign='middle')  
        # label.bind(size=lambda instance, value: setattr(self, 'text_size', value))
        # self.add_widget(label)
        
        
        
        
        
        
        #trash
        # self.outline_color=(1, 0, 0, 1)
        # self.outline_width=2
        
        # self.width = 40
        # self.text_size = (1, 1)
        # self.bind(size=self._update_size)
        # self.size_hint_max = (1, None)
        # self.size_hint = (1, None)
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
    
    #log
    def _update_size(self, instance, value):
        # self.canvas.before.clear()
        # self.size_hint = (1, None)
        # pass
        
        
        if self.parent is not None:
            parent_type = type(self.parent).__name__
            print('Parent type:', parent_type, self.parent.width, self.text[:20] )
            # if parent_type=="MyBoxLayout":
                
            # self.size_hint_max = self.parent.size_hint 
            # self.width = self.parent.width

            
            pass
        else:
            # self.size_hint = (1, None)
            # self.size_hint_max = (1, None)
            pass
        
    # def set_random_background(self):
    #     with self.canvas.before:
    #         # Генерация случайного цвета фона
    #         r, g, b = random(), random(), random()
    #         Color(r, g, b, mode='rgb')
    #         # Нарисовать фоновый прямоугольник
    #         self.rect = Rectangle(pos=self.pos, size=self.size)

    #     self.bind(pos=self.update_background, size=self.update_background)

    # def update_background(self, instance, value):
    #     instance.rect.pos = instance.pos
    #     instance.rect.size = instance.size



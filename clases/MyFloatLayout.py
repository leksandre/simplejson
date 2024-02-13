import kivy
kivy.require('1.0.7')
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle
from random import random

class MyFloatLayout(FloatLayout):
    def __init__(self, componentMbst=False, **kwargs):
        super(MyFloatLayout, self).__init__(**kwargs)
        self.componentMbst = componentMbst
        self.bind(height=self.setter('height'))
        self.bind(size=self._update_background)
        # self.padding=1
        # self.spacing=1
        if componentMbst:
          directionMbst = componentMbst.get('properties',[]).get('direction',False)
          if directionMbst:
            orientation='vertical'
            if directionMbst=='row':
                orientation='horizontal'
            # if directionMbst=='column':#example
            #     orientation='vertical'
            self.orientation = orientation

    def add_widget(self, widget, index=0):
        super(MyFloatLayout, self).add_widget(widget, index)
        self.do_layout()
        
        # self.height = self.height + 60
        
        
        # if self.orientation=='vertical':
        #     self.height = self.height + widget.height 
        
        
        
        
        # if self.orientation=='vertical':
            # self.height = max(child.height for child in self.children)




        # if self.orientation=='vertical':
            # children = self.children
            # max = 0
            # for child in children:
            #     print('Carousel_item_child.height',child.height)    
            #     if child.height>max:
            #         max = child.height
            # self.height = max
            # if self.componentMbst:
            #     print('Carousel final height',self.height,self.componentMbst['properties']['backendname'])

    def _update_background(self, instance, value):
        self.canvas.before.clear()
        with self.canvas.before:
            # Генерация случайного цвета
            r, g, b = random(), random(), random()
            Color(r, g, b, 1)
            # Рисование прямоугольника с цветом фона
            Rectangle(pos=self.pos, size=self.size)
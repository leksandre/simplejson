import kivy
kivy.require('1.0.7')
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
from random import random

class MyBoxLayout(BoxLayout):
    def __init__(self, componentMbst=False, **kwargs):
        super(MyBoxLayout, self).__init__(**kwargs)
        self.bind(minimum_height=self.setter('height'))
        self.bind(size=self._update_background)
        self.componentMbst = componentMbst
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
        super(MyBoxLayout, self).add_widget(widget, index)
        self.do_layout()

    def _update_background(self, instance, value):
        self.canvas.before.clear()
        with self.canvas.before:
            # Генерация случайного цвета
            r, g, b = random(), random(), random()
            Color(r, g, b, 1)
            # Рисование прямоугольника с цветом фона
            Rectangle(pos=self.pos, size=self.size)
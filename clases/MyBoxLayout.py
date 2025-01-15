import kivy
kivy.require('1.0.7')
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
from kivy.utils import get_color_from_hex
from random import random

class MyBoxLayout(BoxLayout):
    def __init__(self, componentMbst=False, **kwargs):
        super(MyBoxLayout, self).__init__(**kwargs)
        self.componentMbst = componentMbst
        self.bind(minimum_height=self.setter('height'))
        self.bind(height=self.setter('height'))
        self.size_hint_y = None #((вот где собака порылась с авторазмерами ячеек))

        # self.bind(size=self._update_background)

        # self.height=0# начнём c нуля, чтоль# !!!!!!!!ошибка!!  пропадут элементы не имеющие свойтсва "размер"
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
          propCssCurrnt = componentMbst.get('properties',[]).get('propCss',False) 
          if propCssCurrnt:

            print("--MyBoxLayout propCssCurrnt", propCssCurrnt)
            for css_prop, value in propCssCurrnt.items():
                    try:
                        if css_prop == 'background-color':
                            print("--MyBoxLayout background-color", value)
    
                            self.background_color = get_color_from_hex(value)
                            with self.canvas.before:
                                Color(*self.background_color)
                                self.rect = Rectangle(size=self.size, pos=self.pos)

                            self.bind(size=self._update_rect, pos=self._update_rect)

                    except Exception as e:
                            print(f"--MyBoxLayout Error processing property '{css_prop}' with value '{value}': {e}")
                       
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



            
        # self.height = self.height + 60
        
        # self.height = 10
        # if self.orientation=='vertical':
        #     self.height = self.height + widget.height +20
        
        
        
        
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

import kivy
kivy.require('1.0.7')
from kivy.uix.stacklayout import StackLayout
from kivy.graphics import Color, Rectangle
from lib import Lib

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
        self.setColor()
        
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

        
        

    def update_rect(self, *args):
        # pass
        self.rect.pos = self.pos
        self.rect.size = self.size

    def setColor(self):
        # попробуем обрабатывать свойства элементов "генерально" (но лучше переделать на "индивитдуально")
        #porcess css
        el = self.componentMbst
        # color = "#337ab7"#для кнопок
        color = "#efeff4"
        # color = (1,1,1,0.1)

        foundColor = Lib.getProperty(el, "background-color")
        if foundColor:
            color = foundColor
        print('componentMbst canvas', color)
        
        with self.canvas.before:
            Color(color)
            # Rectangle(pos=self.pos, size=self.size)
            self.rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self.update_rect, size=self.update_rect)
        
        
        
        











                                      
                # задаём канвас каждому комопненту
                # if uixCmp:
                #     color = "#FFFFFF"
                #     print('componentMbst canvas', color)
                #     with uixCmp.canvas.before:
                #         Color(color)
                #         Rectangle(pos=uixCmp.pos, size=uixCmp.size)
                                        

                # проверяем свойства, вообще у текущего класса етсь только канвах, поэтому нафиг
                    # if hasattr(self, 'background_color'):
                    #     print('componentMbst background_color', color)
                    #     self.background_color = color #(1, 1, 1, 1)   #"white" #(1, 1, 1, 1) #
                    # else:
                    #     if hasattr(self, 'background'):
                    #         print('componentMbst background', color)
                    #         self.background = color #(1, 1, 1, 1) #(color)
                    #     else:
                    #         print('componentMbst canvas', color)
                    #         with self.canvas.before:
                    #             Color(color)
                    #             # Rectangle(pos=self.pos, size=self.size)
                    #             self.rect = Rectangle(pos=self.pos, size=self.size)
                    #         self.bind(pos=self.update_rect, size=self.update_rect)

#надо как-то задать главный фон
        # if content_layout:
        #             color = "#FFFFFF"
        #             print('componentMbst canvas', color)
        #             with content_layout.canvas.before:
        #                 Color(color)
        #                 Rectangle(pos=content_layout.pos, size=content_layout.size)

#надо как-то задать главный фон
        # if content_layout:
        #             # color = "#FFFFFF"
        #             color = (0.9, 0.4, 0.6, 1)
        #             with content_layout.canvas.before:
        #                 Color(color)
        #                 Rectangle(pos=content_layout.pos, size=content_layout.size)
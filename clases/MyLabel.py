import kivy
kivy.require('1.0.7')
from kivy.uix.label import Label
# from clases.MyBoxLayout import MyBoxLayout
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.anchorlayout import AnchorLayout
# from kivy.graphics import Color, Rectangle
# from kivy.uix.scrollview import ScrollView
from kivy.graphics import Color, Rectangle
import time
from kivy.clock import Clock
from random import random
# from clases.MyAnchorLayout import MyAnchorLayout

class MyLabel(Label):
    def __init__(self, text, componentMbst=False, **kwargs):
        super(MyLabel, self).__init__(**kwargs)
        self.componentMbst = componentMbst
      
        self.bind(size=self._update_background)#цвет плашек чтоб наглядно видеть
        self.bind(width=self._update_size)#логи изменений размера
        self.bind(texture_size=self._update_texture_size)
                
        self.height = 100
        # self.height = 10# так в viafdn не пропадают боксы в субфреймах, интересно почему?
        
        self.size_hint = (1, None)
        self.halign='center' 
        self.valign='center'
        self.multiline = True

        self.text = text
     
    def _update_texture_size(self, instance, value):
        def update_text():
                print('self.texture_size[1]',self.texture_size[1])
                self.size[1] = self.texture_size[1]
    
        # print(f'----------', self.text[0:100])
        # print(f'Высота size: {self.size}')
        # print(f'Высота text_size: {self.text_size}')
        # print(f'Высота texture_size: {self.texture_size}')
        if self.texture_size[1]:
         if self.texture_size[1]>10:
             delta = self.texture_size[1] - self.size[1]
             self.size[1] = self.texture_size[1]
            #  print('delta',delta)
            #  self.text_size[1] = self.texture_size[1]
            #  self.spacing = delta
            #  if delta > 0:
            #     #  self.height = self.texture_size[1]
            #      self.height = self.height
            #  if delta < 0:
            #     #  self.height = self.texture_size[1]
            #      self.height = self.height-1
            
        # # self.size[1] = self.texture_size[1]
        # if self.texture_size[1]:
        #  if self.texture_size[1]>10:
        #     # print('self.texture_size[1]',self.texture_size[1])
        #     # self.height = self.texture_size[1]
        #     Clock.schedule_once(lambda dt: update_text(), 2)
        
    def _update_size(self, instance, value):
        try:
            #чтб текст переносился по строкам
            if self.size[0]>10:
                self.text_size[0] = self.size[0]
        except KeyError as e:
            print(' over KeyError  ' + str(e))
            pass
        self._log_parent()

    def _log_parent(self):
         #для дебага
        if False:
        # if True:
          if (self.text).find('111111____11111___Lorem ipsum dolor')>-1:
            if self.parent is not None:
                self_parent=self.parent
                parent_type = type(self_parent).__name__
                print('Parent0 type,height,width:', parent_type, self_parent.height, self_parent.width )
                if self.parent.parent is not None:
                    self_parent=self.parent.parent
                    parent_type = type(self_parent).__name__
                    print('Parent.parent1 type,height,width:', parent_type, self_parent.height, self_parent.width )
                    if self.parent.parent.parent is not None:
                        self_parent=self.parent.parent.parent
                        parent_type = type(self_parent).__name__
                        print('Parent.parent.parent2 type,height,width:', parent_type, self_parent.height, self_parent.width )
                        if self.parent.parent.parent.parent is not None:
                            self_parent=self.parent.parent.parent.parent
                            parent_type = type(self_parent).__name__
                            print('Parent.parent.parent.parent3 type,height,width:', parent_type, self_parent.height, self_parent.width )
                            if self.parent.parent.parent.parent.parent is not None:
                                self_parent=self.parent.parent.parent.parent.parent
                                parent_type = type(self_parent).__name__
                                print('Parent.parent.parent.parent.parent4 type,height,width:', parent_type, self_parent.height, self_parent.width )
                                if self.parent.parent.parent.parent.parent.parent is not None:
                                    self_parent=self.parent.parent.parent.parent.parent.parent
                                    parent_type = type(self_parent).__name__
                                    print('Parent.parent.parent.parent.parent.parent5 type,height,width:', parent_type, self_parent.height, self_parent.width )



    def _update_background(self, instance, value):
        self.canvas.before.clear()
        with self.canvas.before:
            r, g, b = random(), random(), random()
            Color(r, g, b, 1)
            Rectangle(pos=self.pos, size=self.size)




  # 
              #label
        # self.bind(size=self._update_size)


        #так было
        # self.size_hint = (1, None)
        # self.text = text
        # self.height = 40
        # text_size=(1, 1)
        # self.halign='center' 
        # self.valign='center'
        # self.multiline = True
        # self.size_hint = (1, None)
        # self.bind(texture_size=lambda instance, value: setattr(self, 'text_size', value))
        # self.bind(texture_size=lambda instance, value: setattr(self, 'size', value))



        # self.bind(texture_size=lambda instance, value: setattr(instance, 'size', value))

        # новая версия
            


        # if self.parent is not None:
        #     parent_type = type(self.parent).__name__
        #     print('Parent type:', parent_type, self.parent.width, self.text[:20] )
        #     # if parent_type=="MyBoxLayout":
                
        #     # self.size_hint_max = self.parent.size_hint 
        #     # self.width = self.parent.width

            
        #     pass
        # else:
        #     # self.size_hint = (1, None)
        #     # self.size_hint_max = (1, None)
        #     pass



        
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


            # if self.size[1]>10:
            #     self.text_size[1] = self.size[1]

            # time.sleep(0.001)

  

                # нельзя менять забинденое свойство в его бинде
                # self.text_size = self.texture_size
                # self.size = self.text_size
                # self.size = self.texture_size
            

                    # self.canvas.before.clear()
        # self.size_hint = (1, None)
        # pass
            


               # self.text_size=(None, None) 
        
        # self.bind(size=lambda instance, value: setattr(self, 'text_size', value))# перенос строк


        #всякая херня
        # self.bind(size=lambda instance, value: setattr(self, 'width', value[0]))# перенос строк
        # self.bind(texture_size=lambda instance, value: setattr(self, 'height', value[1]))
        # self.bind(texture_size=self.setter('size'))
  # self.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
       
        #   label = Label(text=text, size_hint=(1, None), height=30, text_size=(None, None), halign='left')
        # self.text_size=(1, 1)



      


        
        
        # def update_text():
        #             self.text = text
        # Clock.schedule_once(lambda dt: update_text(), 2)



        # def update_text():
        #      print('self.texture_size',self.texture_size)
        #      self.height = self.height +1
        # Clock.schedule_once(lambda dt: update_text(), 2)

    
        


        
        
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
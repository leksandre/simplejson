import kivy
kivy.require('1.0.7')
from kivy.uix.button import Button
from clases.MyBoxLayout import MyBoxLayout
from kivy.uix.boxlayout import BoxLayout
from lib import Lib
from kivy.utils import get_color_from_hex

class MyButton(Button):
    def __init__(self, text, componentMbst=False, **kwargs):
        super(MyButton, self).__init__(**kwargs)
        self.componentMbst = componentMbst
        
        self.size_hint = (1, None)
        self.height = 50
        
        self.text = text

        # Устанавливаем цвет по умолчанию
        self.setColor()

        # self.setColor()
        # bad idea
        # self.spacing = 1 
        # self.padding=(20, 10, 20, 10)
               
        # btn = Button(text=text)
        # btn.text = text
        # self.add_widget(btn)
        



        self.setFont()

    def setColor(self, color='#347ab7'):
        # попробуем обрабатывать свойства элементов "генерально" (но лучше переделать на "индивитдуально")
        #porcess css
        # el = self.componentMbst
        # color = "#337ab780"
        
        # foundColor = Lib.getProperty(el, "background-color")
        # if foundColor:
        #     color = foundColor
        #     print('componentMbst canvas foundColor', color)


        # print('componentMbst canvas', color)
        self.background_color = get_color_from_hex(color)

    def setFont(self):
        # Устанавливаем шрифт и размер текста
        self.font_size = '11sp'  # Устанавливаем размер текста в sp (scale-independent pixels)
        self.font_name = 'Roboto'  # Устанавливаем шрифт (убедитесь, что шрифт доступен в системе)
        self.halign = 'center'  # Центрируем текст по горизонтали
        self.valign = 'center'  # Центрируем текст по вертикали


        






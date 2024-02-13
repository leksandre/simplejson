from kivy.app import App
from clases.MyBoxLayout import MyBoxLayout
# from clases.MyFloatLayout import MyFloatLayout
from kivy.uix.label import Label
from clases.MyLabel import MyLabel


class LabelsApp(App):
    def build(self):
        # Создание графического интерфейса
        layout = MyBoxLayout(orientation='vertical')
        
        # Создание и добавление виджетов Label
        labels = ['Label 1Label 1Label 1Label 1Label 1Label 1Label 1Label 1Label 1Label 1Label 1Label 1Label 1Label 1Label 1Label 1Label 1Label 1Label 1Label 1Label 1Label 1Label 1Label 1Label 1Label 1Label 1Label 1Label 1Label 1Label 1', 'Label 2Label 2Label 2Label 2Label 2Label 2Label 2Label 2Label 2Label 2Label 2Label 2Label 2Label 2Label 2Label 2Label 2Label 2Label 2Label 2Label 2Label 2Label 2Label 2Label 2Label 2Label 2Label 2Label 2Label 2Label 2Label 2', 'Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3 3Label 3Label 3 3Label 3Label 3 3Label 3Label 3 3Label 3Label 3 3Label 3Label 3 3Label 3Label 3 3Label 3Label 3 3Label 3Label 3 3Label 3Label 3 3Label 3Label 3 3Label 3Label 3 3Label 3Label 3 3Label 3Label 3 3Label 3Label 3 3Label 3Label 3 3Label 3Label 3 3Label 3Label 3 3Label 3Label 3 3Label 3Label 3 3Label 3Label 3 3Label 3Label 3 3Label 3Label 3']
        # for i in range(1,3):
        
        if 1:
          for text in labels:
            label = MyLabel(text=text)
            layout.add_widget(label)
            
        # for text in labels:
        #     label = Label(text=text, size_hint=(1, None), height=30, text_size=(None, None))
        #     layout.add_widget(label)


        return layout


if __name__ == '__main__':
    LabelsApp().run()
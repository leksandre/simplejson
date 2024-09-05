from kivy.app import App
from clases.MyBoxLayout import MyBoxLayout
from clases.MyFloatLayout import MyFloatLayout
from kivy.uix.label import Label
from clases.MyLabel import MyLabel
from clases.MyAnchorLayout import MyAnchorLayout
from clases.MyLabelAnchor import MyLabelAnchor
from clases.MyLabelScroll import MyLabelScroll

from kivy.uix.scrollview import ScrollView


class LabelsApp(App):
    def build(self):
        # Создание графического интерфейса
        anchor_layout = ScrollView()
        layout = MyBoxLayout(orientation='vertical')
        
        
        # Создание и добавление виджетов Label
        labels = ['Label 1Label 1Label 1Label 1Label 1Label 1Label 1Label 1Label 1Label 1Label 1Label 1Label 1Label 1Label 1Label 1Label 1Label 1Label 1Label 1Label 1Label 1Label 1Label 1Label 1Label 1Label 1Label 1Label 1Label 1Label 1', 'Label 2Label 2Label 2Label 2Label 2Label 2Label 2Label 2Label 2Label 2Label 2Label 2Label 2Label 2Label 2Label 2Label 2Label 2Label 2Label 2Label 2Label 2Label 2Label 2Label 2Label 2Label 2Label 2Label 2Label 2Label 2Label 2', 'Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3Label 3 3Label 3Label 3 3Label 3Label 3 3Label 3Label 3 3Label 3Label 3 3Label 3Label 3 3Label 3Label 3 3Label 3Label 3 3Label 3Label 3 3Label 3Label 3 3Label 3Label 3 3Label 3Label 3 3Label 3Label 3 3Label 3Label 3 3Label 3Label 3 3Label 3Label 3 3Label 3Label 3 3Label 3Label 3 3Label 3Label 3 3Label 3Label 3 3Label 3Label 3 3Label 3Label 3 3Label 3Label 3']
        # for i in range(1,3):
        
        if 1:
          for text in labels:
            # label = MyLabelScroll(text=text)
            label = MyLabel(text=text)

            # anchor_layout = MyAnchorLayout(anchor_x='center', anchor_y='top')
            # anchor_layout.add_widget(label)

            # anchor_layout = ScrollView()
            # anchor_layout.add_widget(label)

            layout.add_widget(label)
            
        # for text in labels:
        #     label = Label(text=text, size_hint=(1, None), height=30, text_size=(None, None))
        #     layout.add_widget(label)

        anchor_layout.add_widget(layout)
        return anchor_layout


if __name__ == '__main__':
    LabelsApp().run()
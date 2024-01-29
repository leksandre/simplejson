import kivy
kivy.require('1.0.7')
from kivy.uix.carousel import Carousel

class MyCarousel(Carousel):
    def __init__(self, **kwargs):
        super(MyCarousel, self).__init__(**kwargs)
        self.bind(height=self.setter('height'))

    # def add_widget(self, widget, index=0):
    #     super(MyCarousel, self).add_widget(widget, index)
        
    def on_index(self, instance, value):
        current_widget = self.slides[int(value)]
        # self.size = current_widget.size       
        self.size_hint = (1, None) 
        self.height = self.height+40
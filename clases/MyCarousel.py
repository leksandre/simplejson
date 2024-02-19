import kivy
kivy.require('1.0.7')
from kivy.uix.carousel import Carousel
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

class MyCarousel(Carousel):
    def __init__(self, componentMbst=False, **kwargs):
        super(MyCarousel, self).__init__(**kwargs)
        self.componentMbst = componentMbst
        # self.bind(children=self._on_children_changed)
        # self.bind(height=self.setter('height'))
        # self.bind(on_size=self.update_content_position)
        # self.size_hint_y = None
        self.height = 400

    def add_widget(self, widget, index=0):
        # super(MyCarousel, self).add_widget(widget, index)
        slide1 = ScrollView()#size_hint=(1, None), size=(1, 400)
        
        slide1.add_widget(widget)
        # print('add on Carousel',type(widget).__name__)
        super(MyCarousel, self).add_widget(slide1, index)

        
        # if not isinstance(widget, Label):
        #     raise ValueError("Only Label widgets are allowed in CustomCarousel")
        # super(MyCarousel, self).add_widget(widget, index)

        # super(MyCarousel, self).add_widget(widget, index)

        # slide1 = BoxLayout(orientation='vertical')
        # slide1.add_widget(widget)
        # print('add on Carousel',type(widget).__name__)
        # super(MyCarousel, self).add_widget(slide1, index)
        
    
    
    def update_content_position(self, *args):
        for slide in self.slides:
            slide.y = self.height - slide.height

    def _on_children_changed(self, instance, value):
        children = self.children
        
        # self.height = max(child.height for child in self.children)
        
        # max = 0
        # for child in children:
        #     print('Carousel_item_child.height',child.height)    
        #     if child.height>max:
        #         max = child.height
        # self.height = max
        # if self.componentMbst:
        #     print('Carousel final height',self.height,self.componentMbst['properties']['backendname'])
        
        

    # def on_index(self, instance, value):
    #     current_widget = self.slides[int(value)]
    #     # self.size = current_widget.size       
    #     # self.size_hint = (1, None) 
    #     self.height = self.height+current_widget.height
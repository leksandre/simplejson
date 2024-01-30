import kivy
kivy.require('1.0.7')
from kivy.uix.carousel import Carousel

class MyCarousel(Carousel):


    def add_widget(self, widget, index=0):
        super(MyCarousel, self).add_widget(widget, index)
 
        
    # def on_index(self, instance, value):
    #     current_widget = self.slides[int(value)]
    #     # self.size = current_widget.size       
    #     # self.size_hint = (1, None) 
    #     self.height = self.height+current_widget.height
    
    
    def __init__(self, componentMbst=False, **kwargs):
        super(MyCarousel, self).__init__(**kwargs)
        self.componentMbst = componentMbst
        self.bind(children=self._on_children_changed)
        self.bind(height=self.setter('height'))

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
        
        

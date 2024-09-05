import kivy
kivy.require('1.0.7')
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class MyTextInput(TextInput):
    def __init__(self, text, componentMbst=False, **kwargs):
        super(MyTextInput, self).__init__(**kwargs)
        self.componentMbst = componentMbst
        self.bind(on_text=self.on_text)
        self.multiline=True
        self.do_wrap=True
        self.size_hint_y=None
        self.height=30

        self.text = text
        # print('try self.text', text)
        # print('set self.text', self.text)


        # self.bind(size=self._update_size)#цвет плашек чтоб наглядно видеть
        # self.bind(width=self._update_widht)#логи изменений размера
        # self.bind(height=self._update_height)#логи изменений размера
        # self. =  250
        # print('minimum_height', self.minimum_height)
        # print('readonly', self.readonly)


        # self.line_height=50
        # print('minimum_height', self.minimum_height)
        # print('height', self.height)

        self._log_parent()
        
    def _update_height(self, instance, value):
        print('_update_height',self.height, self.text)

    def _update_widht(self, instance, value):
        print('_update_widht',self.width, self.text)

    def _update_size(self, instance, value):
        print('_update_size',self.size, self.text)

    def on_text(self, instance, value):
        print('on_text', self.text)
        # self.minimum_height = self.height
        
        

    def _log_parent(self):
         #для дебага
        # if False:
        if True:
          if (self.text).find('Loop:GD:backend@ext_col_json:Message')>-1:
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



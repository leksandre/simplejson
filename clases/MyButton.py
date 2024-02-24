import kivy
kivy.require('1.0.7')
from kivy.uix.button import Button
from clases.MyBoxLayout import MyBoxLayout
from kivy.uix.boxlayout import BoxLayout

class MyButton(Button):
    def __init__(self, text, componentMbst=False, **kwargs):
        super(MyButton, self).__init__(**kwargs)
        self.componentMbst = componentMbst
        
 
        
        
        self.size_hint = (1, None)
        self.height = 30
        
        self.text = text
        
        self.setColor()
        # bad idea
        # self.spacing = 1 
        # self.padding=(20, 10, 20, 10)
               
        # btn = Button(text=text)
        # btn.text = text
        # self.add_widget(btn)
        





    def setColor(self):
        # попробуем обрабатывать свойства элементов "генерально" (но лучше переделать на "индивитдуально")
        #porcess css
        el = self.componentMbst
        color = "#337ab780"
        if len(el.get("css",{}).get("all",[]))>0:
            for all in el["css"]["all"]:
                # print('componentMbst css all', all)
                #pocess background-color
                if not isinstance(all,dict):
                    # print('componentMbst css all not is dick', all)
                    print('componentMbst css all not is dick', type(all))
                    continue
                
                if isinstance(all,list):
                    print('componentMbst css all is list', all)
                    continue
                if isinstance(all.get("rules",{}),list):
                    print('componentMbst css all rules is list', all.get("rules",{}))
                    continue

                if len(all.get("rules",{}).get("background-color",[]))>0:
                    color = all["rules"]["background-color"]

                    if color.find("#")==0:
                        color = (color)
                    else:
                        print('original color', color)
                        color =  (0, 0, 0)

                    if len(all.get("selector",[]))>0:
                        parent_type = type(self).__name__
                        print('selector',all["selector"],parent_type)

        print('componentMbst canvas', color)
        self.background_color = color
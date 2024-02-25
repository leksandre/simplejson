class Lib():
   def getProperty(el,name):
        # попробуем обрабатывать свойства элементов "генерально" (но лучше переделать на "индивитдуально")
        #porcess css
        if len(el.get("css",{}).get("all",[]))>0:
            for all in el["css"]["all"]:
                # print('componentMbst css all', all)
                #pocess name
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

                if len(all.get("rules",{}).get("name",[]))>0:
                    color = all["rules"]["name"]

                    if color.find("#")==0:
                        color = (color)
                    else:
                        print('original color', color)
                        color =  (0, 0, 0)

                    if len(all.get("selector",[]))>0:
                        parent_type = type(self).__name__
                        print('selector',all["selector"],parent_type)
                    return color
        return None













            # if len(el.get("css",{}).get("all",[]))>0:
                #     for all in el["css"]["all"]:
                #         # print('componentMbst css all', all)
                #         #pocess background-color
                            # if not isinstance(all,dict):
                            #     # print('componentMbst css all not is dick', all)
                            #     print('componentMbst css all not is dick', type(all))
                            #     continue
                            
                            # if isinstance(all,list):
                            #     print('componentMbst css all is list', all)
                            #     continue
                            # if isinstance(all.get("rules",{}),list):
                            #     print('componentMbst css all rules is list', all.get("rules",{}))
                            #     continue
                #         if len(all.get("rules",{}).get("background-color",[]))>0:
                #             color = all["rules"]["background-color"]

                #             if color.find("#")==0:
                #                 color = (color)
                #             else:
                #                 color =  (0, 0, 0)

                #             if len(all.get("selector",[]))>0:
                #                 parent_type = type(self).__name__
                #                 print('selector',all["selector"],parent_type)
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                   
                    #вынести эту штуку в либу как только станет понятно что делать с атрибутом селектор?
                #универсальная обработка css для всех компонентов
 # попробуем обрабатывать свойства элементов "генерально" (но лучше переделать на "индивитдуально", для каждого класса - свой обработчик)
        #porcess css

                                    
                                    
                                    
                                    
                            # if len(all.get("rules",{}).get("background-color",[]))>0:
                            #     color = all["rules"]["background-color"]

                            #     if color.find("#")==0:
                            #         color = (color)
                            #     else:
                            #         color =  (0, 0, 0)

                            #     if len(all.get("selector",[]))>0:
                            #         parent_type = type(self).__name__
                            #         print('selector',all["selector"],parent_type)
                                    
                                    
                                    
                                        
                        # задаём канвас каждому комопненту
                        # if uixCmp:
                        #     color = "#FFFFFF"
                        #     print('componentMbst canvas', color)
                        #     with uixCmp.canvas.before:
                        #         Color(color)
                        #         Rectangle(pos=uixCmp.pos, size=uixCmp.size)
                                                

                        # # проверяем свойства
                        #     if hasattr(uixCmp, 'background_color'):
                        #         print('componentMbst background_color', color)
                        #         uixCmp.background_color = color #(1, 1, 1, 1)   #"white" #(1, 1, 1, 1) #
                        #     else:
                        #         if hasattr(uixCmp, 'background'):
                        #             print('componentMbst background', color)
                        #             uixCmp.background = color #(1, 1, 1, 1) #(color)
                        #         else:
                        #             print('componentMbst canvas', color)
                        #             with uixCmp.canvas.before:
                        #                 Color(color)
                        #                 Rectangle(pos=uixCmp.pos, size=uixCmp.size)
                        #             uixCmp.bind(pos=uixCmp.update_rect, size=uixCmp.update_rect)

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
                            






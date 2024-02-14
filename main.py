import kivy
kivy.require('1.0.7')

from some import API_KEY, pgdb, pguser, pgpswd, pghost, pgport, pgschema, url_a, url_l, urlD, log_e, pass_e, managers_chats_id, service_chats_id, AppId, ObjectId, url_hash_objects, url_hash_filters_events,url_refresh

from clases.MyBoxLayout import MyBoxLayout
from clases.MyFloatLayout import MyFloatLayout
from clases.MyCarousel import MyCarousel
from clases.MyButton import MyButton
from clases.MyLabel import MyLabel
from clases.MyLabelScroll import MyLabelScroll
from clases.MyStackLayout import MyStackLayout

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.videoplayer import VideoPlayerAnnotation
from kivy.uix.videoplayer import VideoPlayer
from kivy.storage.jsonstore import JsonStore
from kivy.uix.image import AsyncImage
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView


# import cv2
import sys
# import m3u8
# import tkinter as tk
# import numpy as np
# from PIL import Image
import os
from datetime import datetime
import random
import time
import requests
import json
import html2text
import re
import validators
import pprint

store = JsonStore(f'appid_{AppId}_objid_{ObjectId}')

hashtags = []

if store.exists('#object#'):
    hashtagsS =  store.get('#object#')
    # print('-------------- hashtags exists:', hashtagsS)
    print('-------------- object exists:', json.dumps(hashtagsS)[:500])
    
    # hashtags = list(hashtagsS)
    
    # for item in store.find(name='Object'):
    #     print('data 0')
    # for item in store.find(name='#EventsFilter:GD:Data#'):
    #     print('data 1')
    # for item in store.find(name='#EventsFilter:MyGD:Data#'):
    #     print('data 2')


for key, value in store.find():
    print('-------- store item', key)
    # print('-------- store item', "!_"+key+"_!")
    # store.delete(key)
        
def processHashtagData(data):
    for element in data:
        # if 1:
        #     print('element data',element)#!!!
        if 'type' in element:
            # print('______ type data')
            if 'id' in element:
                # print('______ id element')
                if 'attributes' in element:
                    attributes = element['attributes']
                    # print('______ add to store '+element['type'],attributes)
                    
                    # store['hashtags_'+element['type']][element['type']] = {id:element['id'], **attributes}
                    
                    store.put('#'+(element['type']).lower()+'#', name=element['type'], id=element['id'], **attributes)

        else:
            if 'id' in element:
                # print('______ id element')
                if 'attributes' in element:
                    # print('______ attributes element')
                    attributes = element['attributes']
                    if 'tag' in attributes:
                        # store['hashtags_'+attributes['tag']][attributes['tag']] = {data:attributes['data']}
                        # print('______ add to store '+ (attributes['tag']).lower() )
                        store.put((attributes['tag']).lower(), name=attributes['tag'], data=[attributes['data']])  
                        
                        # # store['hashtags'][attributes['tag']] = {data:{k: v for v, k in enumerate([attributes['data'][0]])} }
                        # if len(attributes['data'])>0:
                        #     store['hashtags'][attributes['tag']] = {data:[attributes['data'][0]] }
                        # #  store.put('hashtags', name=attributes['tag'], data=[attributes['data'][0]])  
                        # else:
                        #  store.put('hashtags', name=attributes['tag'], data=[attributes['data']])  
                            
    
    # for item in store.find():
    #     print('tshirtmans item', item)
    
from kivy.config import Config
Config.set('graphics', 'width', '100')
Config.set('graphics', 'height', '400')

from kivy.core.window import Window
Window.size = (600, 1000)
# Window.clearcolor = (1.0, 1.0, 1.0, 1.0)

# config 
execution_path = os.getcwd()


global access_token
access_token = ''
global refresh_token
refresh_token = ''

if store.exists('auth'):
    auth = store.get('auth')
    print('--------------  auth exist:', auth)
    access_token =  auth['access_token']
    refresh_token =  auth['refresh_token']

    
# get
# curl 'https://viafdn-admin.mobsted.com/api/v8/screen?ApplicationId=18&page=1&pageSize=200&uni=1705579847214' \
    
    
def simpleRequest(isGet = False, checkStruct = False, showresp = False, **params):
        try:
            if isGet:
                r = requests.get(**params)
            else:
                # print('post params',params)
                r = requests.post(**params)
        except requests.exceptions.RequestException as err:
            print("__OOps: Something Else", err)
            #return Response1("201", '')
            return False
        except requests.exceptions.HTTPError as errh:
            print("__Http Error:", errh)
            #return Response1("201", '')
            return False
        except requests.exceptions.ConnectionError as errc:
            print("__Error Connecting:", errc)
            #return Response1("201", '')
            return False
        except requests.exceptions.Timeout as errt:
            print("__Timeout Error:", errt)
            #return Response1("201", '')
            return False
        except KeyError as e:
            print(' over KeyError  ' + str(e))
            #return Response1("201", '')
            return False
        if showresp:
            print('result text:'+str(r.text))
            print('response:', (r))
            print('response type:', type(r))
        
        print('status_code:'+str(r.status_code))
        
        if r.status_code == 501 and (str(params['url']).find('/api/v8/refresh')>-1):# if token fail
            time.sleep(random.randint(2,5));
            return auth(force = 1)
            
        if r.status_code == 401:# if token expired
            print('--------- try refresh token')
            res_refresh = refresh_auth()
            if not res_refresh:
                res_auth = auth()
                if res_auth:
                    return simpleRequest(isGet, checkStruct, showresp, **params)
            
        if r.status_code != 200:
            print('text:'+str(r.text)[0:2000])
            try:
                print(html2text.html2text(r.text))                     
            except KeyError as e:
                print(' not json as text KeyError  ' + str(e))
            print('params',params)
            return False
        
        # d = json.JSONDecoder()
        
        try:
            data = json.loads(r.text)
        except json.JSONDecodeError:
            print(' not json 0 ' + str(r.text)[0:200])
            try:
                print(html2text.html2text(r.text))                     
            except KeyError as e:
                print(' not json as text KeyError  ' + str(e))
            print('params',params)
            return False
        
        if checkStruct:
            if not 'data' in data:
                print(' not data 0 ' + str(data))
                print('params',params)
                return False
            if not 'meta' in data:
                print(' not meta 0 ' + str(data))
                print('params',params)
                return False
            for dataList in data['data']:
                print(' data[data] ',dataList)
        
        return r

def getScreens(tables=[]):
    global structable
    Headers = { 'Authorization' : "Bearer "+str(access_token) }
    
    listId = 0

    r = simpleRequest(isGet=True, url = urlD+url_l+f"?ApplicationId={AppId}&page=1&pageSize=200", headers=Headers)

    try:
        if not r:
            print('r',r)
            return False
        data = r.json()
    except:
        return False
    
    data = r.json()
    # print('data json 1',data)
    
    # for dataList in data['meta']:
    #     print('dataList',dataList)
        
    # for dataList in data['data']:
    #     print('dataList',dataList)

    return data

def refresh_auth():
    global access_token
    global refresh_token
    
    if len(refresh_token)==0:
        False
        
    url_e = urlD+(url_refresh.replace('ref_token',refresh_token))
    
    print('--------- try refresh token')
    
    r = simpleRequest(isGet=True, url = url_e)

    try:
        if not r:
            print('r',r)
            return False
        data = r.json()
    except:
        return False
    
    # print('data json 0',data)
    if not 'access_token' in data:
        print('!!! not access_token ' + str(data))
        return False
    try:
        access_token = data['access_token']
        refresh_token = data['refresh_token']
        store.put('auth', 
        access_token = data['access_token'],
        refresh_token = data['refresh_token'])
        
        # print('tokens - ',data,access_token,refresh_token)
    except KeyError as e:
        print('!!! over KeyError 43 ' + str(e))
        return False
    return r
    
def auth(force = False):
    global access_token
    global refresh_token
    
    if not force:
        if len(access_token)>0:
            return True
    
    PARAMS = {'login':log_e,'password':pass_e}
    url_e = urlD+(url_a.replace('userLogin555',log_e)).replace('userPassword888',pass_e)
    
    r = simpleRequest(isGet=True, url = url_e, params = PARAMS)
    
    try:
        if not r:
            print('r',r)
            return False
        data = r.json()
    except:
        return False
    
    # print('data json 0',data)
    if not 'access_token' in data:
        print('!!! not access_token ' + str(data))
        return False
    try:
        access_token = data['access_token']
        refresh_token = data['refresh_token']
        store.put('auth', 
        access_token = data['access_token'],
        refresh_token = data['refresh_token'])
        # print('tokens - ',data,access_token,refresh_token)
    except KeyError as e:
        print('!!! over KeyError 43 ' + str(e))
        return False
    return r

def processComponents(component, ui_components, loopdata={}):
    if 'components' in component:
        
    #  #debug   
    #  if component.get('properties',{}).get('backendname',{}):
    #     if component['properties']['backendname'] == 'SlideItem-f5f504c8':
    #         print("draw_mbst_slider_slide",component['properties']['backendname'])
                
                
     for elemData in component['components']:
        # print('!!-- Carousel slide item aliasName',elemData['aliasName'])
        # print('!!-- Carousel slide item name',elemData['name'])
        # print('- ',elemData)
        
        # #debug   
        # if component.get('properties',{}).get('backendname',{}):
        #     if component['properties']['backendname'] == 'SlideItem-f5f504c8':
        #         print("elemData",elemData['properties']['backendname'])
                
        if 1:
            foradding = processComponent(elemData, loopdata=loopdata)
            addItTo(ui_components[0], foradding)
    


def addItTo(loca, foradding):
    if foradding:  
        if isinstance(foradding,list):
            for iten in foradding:
                loca.add_widget(iten)
        else:
            loca.add_widget(foradding)

def processItems(component, ui_components, loopdata={}):
    if 'items' in component:
      fullColWidth = 12# мы так давным давно решили
        
    # если мы когда инбудь откажемся от 12теричной системы колонок то надо удет использовать подоный алгоритм
    #   fullColWidth = 0  
    #   for elem in component['items']:
    # # специально для высчитывания ширины колнок во flexrow 
    #    if elem.get('properties',{}).get('colwidth',{}):
    #     fullColWidth += int(elem['properties']['colwidth'])
        
      for elem in component['items']: # если это стурктура с items
       curColWidth = -1 
    #    print('!!--aliasName',elem['aliasName'])
    #    print('!!--name',elem['name'])
       if elem.get('properties',{}).get('colwidth',{}):
        # print('!!--colwidth',elem['properties']['colwidth'])
        if fullColWidth>0:
            curColWidth = int(elem['properties']['colwidth'])/fullColWidth
    
       # варинат 1 отправляем в "конвейер", т.е. создаём "бокс" для каждого элемента из items и обрабатываем его содержимое соответственно "линейно", но без влияния на родительский компонент
       foradding = processComponent(elem, size_hint = curColWidth, loopdata=loopdata)
       addItTo(ui_components[0], foradding)
    #    if foradding:
    #     ui_components[0].add_widget(foradding)
    
        
       # вариант 2 сами реагируем на структуру компонента пропуская обработку элементов "обёрток" mbst-slider__slide mbst-flexrow__col
    #    if 'components' in elem:
    #     for elemData in elem['components']:
    #         # print('- ',elemData)
    #         if 1:
    #             foradding = processComponent(elemData)
    #             if foradding:
    #                 ui_components[0].add_widget(foradding)

# def draw_mbst_slider(component): #has items!
#     # print("------component Slider Carousel ['css']",component['css'])
#     carousel = Carousel(direction='right',size_hint = (1, None), opacity=0.50 )
#     processItems(component,[carousel])              
#     return carousel

# def draw_mbst_slider_slide(component):
#     elem = MyBoxLayout(orientation='vertical',size_hint=(1, None))#, minimum_height=10
#     # elem = GridLayout(cols=1, spacing=10, minimum_height = 200)
#     processComponents(component,[elem])
#     return elem

def draw_mbst_slider_slide(component, loopdata={}):
    elem = MyBoxLayout(orientation='vertical',size_hint=(1, None), componentMbst = component)#, minimum_height=10, spacing=20
    # elem.bind(minimum_width=elem.setter('width'))
    # elem.bind(minimum_height=elem.setter('height'))
    # elem.bind(minimum_size=elem.setter('size'))
    # elem = GridLayout(cols=1, spacing=10, minimum_height = 200)

    processComponents(component,[elem])
    
    # if 'backendname' in component['properties']:
    #             print('backendname slider',component['properties']['backendname'])
    
    # вручную высчитываем необходимую высоту элемента
    # if 'backendname' in component['properties']:
    #     print('backendname',component['properties']['backendname'])
    #     children = elem.children
    #     for child in children:
    #         print('Carousel_item_child.height',child.height)    
    #         elem.height = elem.height+child.height
    #     print('final height',elem.height,component['properties']['backendname'])   
        
    return elem


        

                    
def draw_mbst_slider(component, loopdata={}): #has items!
    # print("------component Slider Carousel ['css']",component['css'])
    carousel = MyCarousel(direction='right',size_hint = (1, None), opacity=0.50, componentMbst = component )
    
    
    # carousel = MyBoxLayout(orientation='vertical',size_hint = (1, None), opacity=0.50 )
    
    # carousel.bind(minimum_height=carousel.setter('height'))
    processItems(component,ui_components=[carousel], loopdata=loopdata)
    # TabbedPanel #??????
    
     # вручную высчитываем необходимую высоту элемента
    # if 'backendname' in component['properties']:
    #     print('backendname',component['properties']['backendname'])
    #     children = carousel.children
    #     for child in children:
    #         print('Carousel_child.height',child.height) 
    #         carousel.height = carousel.height+child.height
    #     print('final height',carousel.height,component['properties']['backendname'])
           
    return carousel

def draw_mbst_flexrow_col(component, size_hint = 0, loopdata={}):
    # print("component Col ['css']",component['css'])
    
    #debug
    # if component.get('properties',{}).get('backendname',{}):
        # if component['properties']['backendname']=='cell-be760fbc':
        #     print("component Col ['properties']['backendname']",component['properties']['backendname'], size_hint)
        #     if size_hint==-1:
        #         print("component Col 1")
        #     if size_hint==0.0:
        #         print("component Col 0.0")
        #     if size_hint>0:
        #         print("component Col >0")
                
    if size_hint==-1:
        return False
    if size_hint==0.0:
        return False
    
    if size_hint>0:
        elem = MyBoxLayout(orientation='vertical', size_hint=(size_hint, None), componentMbst = component) #size_hint_max=(size_hint, None),
 
        # if 'backendname' in component['properties']:
        #     print('backendname final size_hint',component['properties']['backendname'], size_hint)
        #, minimum_height=10
    else:
        elem = MyBoxLayout(orientation='vertical',size_hint=(1, None), componentMbst = component)#, minimum_height=10
    # elem.bind(minimum_height=elem.setter('height'))
    processComponents(component,[elem])
    
     # вручную высчитываем необходимую высоту элемента
    # if 'backendname' in component['properties']:
    #     print('backendname',component['properties']['backendname'])
    #     children = elem.children
    #     for child in children:
    #         print('flexrow_item_child.height',child.height)    
    #         elem.height = elem.height+child.height
    #     print('final height',elem.height,component['properties']['backendname'])   
        
    return elem


def draw_mbst_flexrow(component, loopdata={}): #has items!
    layout = MyStackLayout(orientation='lr-tb', size_hint=(1, None), componentMbst = component) #, minimum_height=100, size_hint=(None, None), size=(400, 400)
    
    processItems(component, ui_components = [layout], loopdata=loopdata)
    
     # вручную высчитываем необходимую высоту элемента
    # if 'backendname' in component['properties']:
    #     print('backendname',component['properties']['backendname'])
    #     children = layout.children
    #     for child in children:
    #         print('flexrow_child.height',child.height)    
    #         layout.height = layout.height+child.height
    #     print('final height',layout.height,component['properties']['backendname'])   
        
    return layout

def draw_mbst_video_player(component):
    return False
    # print("-component properties ['properties']['source'] ",component['properties']['source'])
    # player = VideoPlayer(source='myvideo.avi', state='play',options={'eos': 'loop'}) #VideoPlayerAnnotation
    player = VideoPlayer(source='myvideo.avi', state='play',options={'fit_mode': 'contain'})
    return player

def draw_mbst_button(component):
    # print("component Button ['css']",component['css'])
    btnSimple = MyButton(text=component['properties'].get('text', ""), componentMbst = component) # , size_hint=(1, None), height=10, width=10, padding=(2,2), line_height = 10
    # btn2e.bind(on_press=)
    # btn2e.bind(on_release=)
    return btnSimple

def draw_mbst_image(component):
    this_url = False
    if component.get('properties', {}).get('image', {}).get('url', {}):
        try:
            this_url = component['properties']['image']['url']
            print("-------component properties 0 ['properties']['image']'url' ", this_url)
        except KeyError as e:
            print(' KeyError  ' + str(e))
    else:    
      try:
        if component.get('properties', {}).get('image', {}).get('attributes', {}).get('Url', {}):
            this_url = component['properties']['image']['attributes']['Url']
            print("-------component properties 1 ['properties']['image']['attributes']'url' ", this_url)
      except AttributeError as e:
            print(' KeyError  ' + str(e))
        
    # if component.get('properties', {}).get('backendname', {}):
    #     bn = component['properties']['backendname']
    #     if bn == 'Image-384508c6':
    #         print("component image ['properties']['backendname']",bn)
    #         print(component['properties']['image']['attributes']['Url'])
        
    # wimg = Image(source='mylogo.png')
    # aimg = AsyncImage(source='https://viafdn-admin.mobsted.com/tenants/viafdn/uploads/2021/7/20/20095bc04ac1dfe4b3337d10caa77ca9.png')
    
    if this_url:
      if validators.url(this_url):
        aimg = AsyncImage(source=this_url)
        return aimg
    return False
    
def draw_mbst_text(component):
    label = MyLabel(text=component['properties'].get('text', ""), componentMbst = component)#, padding = 10, line_height=20
    # btn2e.bind(on_ref_press=)
    return label
    
def draw_mbst_text_area(component):
    textinput = TextInput(text=component['properties'].get('text', ""), multiline=True, do_wrap=True)
    # textinput.bind(on_text_validate=on_enter)
    # textinput.bind(text=on_text)
    return textinput

def draw_mbst_link(component):
    # widget = Label(text='Hello [ref=world]World[/ref]', markup=True)
    widget = MyLabel(text=component['properties'].get('text', ""), componentMbst = component)
    # , padding=10
    # widget.bind(on_ref_press=print_it)
    return widget

def try_parse_int(value):
    try:
        result = int(value)
        return result
    except ValueError:
        return None
    
def processHtOnComponent(component, loopdata):
    
    text = json.dumps(component)
    ht = extractHtFromDict(text)
    
    for h in ht:
        # print('ht --',h)
        p_ht = h.split(':')
        if len(p_ht)>1:
            if store.exists('#'+p_ht[0].lower()+'#'):
                ht_v = store.get('#'+p_ht[0].lower()+'#')
                if p_ht[1] in ht_v:
                    # print('tag found ',h,'=>',p_ht[1],'=>',ht_v.get(p_ht[1]))
                    text = text.replace('#'+h+'#',ht_v.get(p_ht[1]))


            # работа с за лупами
            if p_ht[0].lower()=='loop':
                # print('ht loop --',h)
                if p_ht[1].lower() in loopdata:
                    my_dict = loopdata[p_ht[1].lower()]
                    if p_ht[2] in my_dict:
                        if 'backend@files'==p_ht[2]:
                            print('backend@files',h,type(my_dict[p_ht[2]]))
                        if isinstance(my_dict[p_ht[2]],dict):
                          if p_ht[3] in my_dict[p_ht[2]]:
                              text = text.replace('#'+h+'#',my_dict[p_ht[2]][p_ht[3]])

                        if isinstance(my_dict[p_ht[2]],str):
                              text = text.replace('#'+h+'#',my_dict[p_ht[2]])

                        if isinstance(my_dict[p_ht[2]],list):
                            # print('ht list loop --',h)
                            index1 = try_parse_int(p_ht[3])
                            if index1:
                             if index1 not in my_dict[p_ht[2]]:
                                 print('error index',h)
                             if index1 in my_dict[p_ht[2]]:
                              if isinstance(my_dict[p_ht[2]][index1],dict):
                                if p_ht[4] in my_dict[p_ht[2]][p_ht[3]]:
                                    text = text.replace('#'+h+'#',my_dict[p_ht[2]][p_ht[3]][p_ht[4]])

                        # if isinstance(my_dict[p_ht[2]],int):
                        #   print('ht loop --',h, p_ht[2], my_dict[p_ht[2]]) 
                        # else:        
                        #   if len(my_dict[p_ht[2]])>0:
                        #     print('ht loop --',h, p_ht[2], my_dict[p_ht[2]]) 





                    # print('ht loop count vals --',len(my_dict))
                    # first_key = next(iter(my_dict))
                    # first_value = my_dict[first_key]
                    # print('ht loop vals --',first_value )
                    
                    

            # else:
            #     print('tag not found',('#'+p_ht[0].lower()+'#'))


    try:
        componentNew = json.loads(text)
        if componentNew:
            # print(' ret new compotetn  ')
            return componentNew                
    except KeyError as e:
        print(' not json as text KeyError  ' + str(e))
                

    return component


def createComponentUix(el, size_hint=0, loopdata={}):
    if not 'name' in el:
        return False
    # отрисовываем компоненты и возврщаем их вызвавшему родительскому компоненту
    if el['name'] == 'mbst-flexrow':
        return draw_mbst_flexrow(el, loopdata=loopdata)
    if el['name'] == 'mbst-slider':
        return draw_mbst_slider(el, loopdata=loopdata)
    # подэлементы от flexrow и slider
    if el['name'] == 'mbst-flexrow__col':
        return draw_mbst_flexrow_col(el, size_hint, loopdata=loopdata)
    if el['name'] == 'mbst-slider__slide':
        return draw_mbst_slider_slide(el, loopdata=loopdata) 


    if 'items' in el:
        print('has more items!!!')
    
    if el['name'] == 'mbst-button':
        return draw_mbst_button(el)
    if el['name'] == 'mbst-text':
        return draw_mbst_text(el)
    if el['name'] == 'mbst-image':
        return draw_mbst_image(el)
    if el['name'] == 'mbst-text-area':
        return draw_mbst_text_area(el)
    if el['name'] == 'mbst-link':
        return draw_mbst_link(el)
    if el['name'] == 'mbst-video-player':
        return draw_mbst_video_player(el)

    #drawers
    if el['name'] == 'mbst-drawer-left':
        pass
    if el['name'] == 'mbst-drawer-right':
        pass

def getLoopDataset(nameDataset):
    # return None
    # for key, value in store.find():
    #     print('-------- store item', key)
    #     if key == nameDataset:
    #         print('!!!!!!!!!')
     
    # print('dataSource - try to get', nameDataset)

    #  for k,v in store.find(name=nameDataset):
    #      print('dataSource - k', k)
    #      print('dataSource - len', len(v))

    #  for k,v in store.find(name="#eventsfilter:mygd:data#"):
    #      print('dataSource - k', k)
    #      print('dataSource - len', len(v))

    # for k,v in store.find(name=nameDataset): # cтал приводить хранилище в к нижнему регистру и сразу это перестало работать
    for k, v in store.find(): # прихордиться руками перебирать стор
      if k == nameDataset:# прихордиться руками перебирать стор
        # print('-------- store item', key)
        # if 1:
        #     print('dataSource found')
        #     print('dataSource len k', len(k))
        #     print('dataSource type k', type(k))
        #     print('dataSource len v', len(v))
        #     print('dataSource type v', type(v))

        # print('!!!!!!!!!')
        if isinstance(v, str):
            print(f"v = {v}") # такого вообще не бывает
        if isinstance(k, str):
            print(f"k = {k}") # здесь имя которое мы задали в name когда мы сохраняли в store
        if isinstance(v, dict):
            for v0 in v.items():
                # print(f"v0 = {type(v0)}")
                if isinstance(v0, tuple):
                    for element in v0:
                        # print(type(element))
                        # if isinstance(element, str):
                        #     print(type(element), " 1 -- 200 ",element[0:200]) # здесь открывается секция data
                        if isinstance(element, list):
                            if isinstance(element[0], list):
                                # try:
                                #     print(" type [0] ", type(element[0]), " [0][0] ", type(element[0][0]))
                                # except:
                                #     print(f'ValueError row ')
                                #     continue
                                # if isinstance(element[0][0], dict):
                                if 1:
                                    for line in element[0]:
                                        yield line

                    # [print(type(element)) for element in v0]
                    # print(*v0, sep="\n\n\n <-> \n\n\n")

            # for k,v0 in v:
            #     print(f"{k}=>{v0}")

        # for item in items:
        #     print('dataSource len item', len(item))
        #     t = type(item)
        #     print('dataSource type item', t)
        #     if isinstance(item, str):
        #         print(item[0:200])
        #     if isinstance(item, dict):
        #         for v in item:
        #             print(f"{v}")

        #         try:
        #             for k,v in item:
        #                 print(f"{k}=>{v}")
        #     #    except KeyError as e:
        #     #        pass
        #         except ValueError as e:
        #             print(f'ValueError row '+ str(e))
        #             continue
            
            
    
def processComponent(component, size_hint = 0, loopdata = {}):

    # for elem in component:
    #     print('-component',elem)
    # print('-component properties',component['properties'])
        
    el = component
    
    # if 'properties' in el:
    #     if 'source' in el['properties']:
    #         print('- source properties',el['properties']['source'])
    #     if 'dataSource' in el['properties']:
    #         print('- dataSource properties',el['properties']['dataSource'])
    
    # if 'source' in el:
    #     print('- source',el['source'])
    # if 'dataSource' in el:
    #     print('- dataSource',el['dataSource'])
    
    # if 'loop' in el:
    #     if 'source' in el['loop']:
    #         print('- loop source',el['loop']['source'])
    #     if 'dataSource' in el['loop']:
    #         print('- loop dataSource',el['loop']['dataSource'])
    
    aliasName = ''
    loopdataGenerator = [{}]

    isloop = False
    if 'properties' in el:
        if 'loop' in el['properties']:
            # if 'source' in el['properties']['loop']:
            #     print('- source loop properties',el['properties']['loop']['source'])
            if 'dataSource' in el['properties']['loop']:
                if 'aliasName' in el['properties']['loop']:
                    if el['properties']['loop']['dataSource'] and el['properties']['loop']['aliasName'] :
                        nameDataset = (el['properties']['loop']['dataSource']).lower() 
                        aliasName = (el['properties']['loop']['aliasName']).lower() 

                        # print( '- dataSource loop properties',nameDataset)
                        # print( '- dataSource loop properties',aliasName)
                        # loopdataGenerator = getLoopDataset(nameDataset) # передават по цепочке генератор или передавать весь лист значений?

                        loopdataGenerator = list(getLoopDataset(nameDataset)) # пока поработам с обычнцми листами, потом если что, перейдем на генераторы (один хер объёмы резевируемой памяти не изменяться)
                        # pprint.pprint( loopdataGenerator) 
                        # print('loopdataGenerator:',type(loopdataGenerator))

                         



    # if loopdata:
    #     print('loopdata',len(loopdata))
    # print('css',el['css'])
    # print('config',el['config'])
    # if 'uuid' in el:
    #     print('uuid',el['uuid'])
                        
    uixCmpList = []                    
    for line1 in loopdataGenerator:

        # pprint.pprint('line1', line1)
        # if aliasName:
        #     print('____aliasName____', aliasName)

        if len(aliasName)>0:
            loopdata[aliasName] = line1 # да, блин, кажется надо сохранять все данные для лупа в лист и никаких генераторов... вроде бы

        #было
        # el = processHtOnComponent(el)#заменяем хештеги
        # uixCmp = createComponentUix(el, size_hint)

        #стало, переходим на лупы
        el = processHtOnComponent(el, loopdata=loopdata)#заменяем хештеги
        uixCmp = createComponentUix(el, size_hint, loopdata=loopdata)   

        if uixCmp:
            try:
                pass
                # uixCmp.minimum_height = 20 # BoxLayout.minimum_height  #GridLayoutminimum_height 
                # uixCmp.height = 120
                # uixCmp.line_height = 120 # Label.line_height
                # uixCmp.line_height = 120 # TextInput.line_height
                # uixCmp.minimum_height = 120 # TextInput.minimum_height
                #Widget.height
                # uixCmp.size_hint=(1, None)
            except AttributeError:
                pass
            uixCmpList.append(uixCmp) #тут тоже можно возврщать генератор, но надо ли....
        
    
    # try:
    #     print('!-aliasName',el['aliasName'])
    #     print('!-name',el['name'])
    # except AttributeError:
    #     pass
    return uixCmpList



                     
            

def getHashTags(screenId, ht):
    if screenId==0:
        return {}
    Headers = { 'Authorization' : "Bearer "+str(access_token), 'Content-Type':"application/json" }
    
    objectHt = list(filter(lambda x: x.lower().startswith('object:'), ht))
    if len(objectHt)>0:
        fullHt = ["#"+str(x)+"#" for x in objectHt]
        # print('objectHt',objectHt)
        # print('fullHt',fullHt)
        json_details = {
            "applicationId": AppId,
            "ids": [500],
            "tags":fullHt
            # "tags":["#Object:FirstName#","#Object:CompanyAccount#","#Object:Image#"]
        }
        maindata =  json.dumps(json_details) 
        r = simpleRequest(url = urlD+url_hash_objects, headers=Headers, data=maindata) # example of body  --data-raw '{"ids":[500],"applicationId":18,"tags":["#Object:FirstName#","#Object:CompanyAccount#","#Object:Image#"]}'
        if not r:
            return {}

        # print(r)
        data = r.json()
        print(data)
        print('len(data)1 ',len(r.text))
        if not 'data' in data:
            print(' not data 1 ' + str(data))
            return False
        processHashtagData(data['data'])


    # store.put('hashtags', name='Object', org='kivy')
    # store['hashtags'] = {'name': 'Mathieu'}
    # hashtags.append
    
    
    eventsFilterHt = list(filter(lambda x: x.lower().startswith('eventsfilter:'), ht))
    if len(eventsFilterHt)>0:
        fullHt = [ {"tag": "#"+str(x)+"#", "objectId": ObjectId, "pagination": {"page": 1, "pageSize": 10, "showButtonUp": False, "showInformer": True}} for x in eventsFilterHt]
        print('eventsFilterHt',eventsFilterHt)
        print('fullHt',fullHt)
        json_details = {"applicationId": AppId, "objectId": ObjectId, "extraParams": {"Screen": {
            "id": screenId}, "Globals": {"applicationId": AppId, "objectId": ObjectId}}, "tags": fullHt}

        maindata =  json.dumps(json_details) 
        
        r = simpleRequest(url = urlD+url_hash_filters_events, headers=Headers, data=maindata)  # example of body  --data-raw '{"applicationId":18,"objectId":500,"extraParams":{"Tenant":{},"Application":{},"Screen":{"id":49,"ApplicationId":18,"SortOrder":0,"Name":"Home screen","UpdateDate":"2021-05-19 08:11:18.695368","CreateDate":"2021-05-19 08:11:18.695368","uuid":"ba1db960-178a-410c-833a-0d675e1e296b","LastModified":"2024-01-12 07:31:04.286629","ishomescreen":True,"name":"mbst-screen","aliasName":"Screen"},"Object":{"FirstName":"Aleksandr I","CompanyAccount":"0","Image":"https://viafdn-admin.mobsted.com/tenants/viafdn/uploads/2021/7/7/6361866df06e28611bb3a3e8bea8d15f.png","FacebookChannel":null,"ChromePush":null,"Points":"0","Range":"The Helpful Citizen"},"Variable":{"MenuMS":"0","MenuR":"0","MenuMKL":"0","ShowEdit":"0","HeartPopup":"20240122","PushWidget":"on"},"Payment":{},"Backendname":{"EditAct2#Loop:GD:backend@id#":"#Loop:GD:backend@ext_col_json:Message#"},"LastEvent":{},"Route":{"path":"/18/","query":{"appid":"18","screenid":"49","objid":"500","os":"ios"},"params":{"appid":"18"}},"Tax":{},"Globals":{"applicationId":18,"objectId":500}},"tags":[{"tag":"#EventsFilter:MyGD:Data#","objectId":500,"pagination":{"page":1,"pageSize":10,"showButtonUp":False,"showInformer":False}},{"tag":"#EventsFilter:GD:Data#","objectId":500,"pagination":{"page":1,"pageSize":10,"showButtonUp":False,"showInformer":True}}]}'
        
        if not r:
            return {}

        # print(r)
        data = r.json()
        print(r.text[0:200])
        print('len(data) 0 ',len(r.text))
        if not 'data' in data:
            print(' not data 1 ' + str(data))
            return False
        processHashtagData(data['data'])
    
    return {}
    
    
def filterTags(x):
    # if x.lower().startswith('loop:'):
    #     return False
    if x.lower().startswith('variable:'):
        return False
    if x.find(':')==-1:
        return False
    return True

def extractHtFromDict(screen):
    if type(screen)=='text':
        text = screen
    else:
        text = json.dumps(screen)

    # if text.find('#Loop:')>-1:
    #     print('-- #Loop: text screen',text[text.find('#Loop:')-10:text.find('#Loop:')+100])

    foundHt = []
    try:
        found = re.findall(r"#([\w:@]*)#", text)
        found = list(set(found))
        foundHt = list(filter(lambda x: filterTags(x), found))
    except AttributeError:
        pass

    # if foundHt:
    #     print('found', foundHt)
        
    return foundHt

def parseScreen(screen):
    scrollable_content = ScrollableContent(screen)
    
    # если понадобится дополнительный коневрой элемент 
    # root_layout = MyBoxLayout(orientation='vertical', size_hint=(1, 1))
    # root_layout.bind(minimum_height=root_layout.setter('height'))
    # root_layout.add_widget(scrollable_content)
    return scrollable_content
 
    
    
    
    
# классы
    
    
    
    


        


# будем класть в корень ScrollView, но, если что, можно и BoxLayout, для некоторых реализаций он будет даже удобнее, главное не забыть положить на него наш ScrollView
class ScrollableContent(ScrollView):#BoxLayout
    def __init__(self, screen, **kwargs):
        super(ScrollableContent, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.size_hint=(1, 1)

        content_layout = MyBoxLayout(orientation='vertical', size_hint=(1, None))#, spacing=0
        # content_layout.bind(minimum_height=content_layout.setter('height'))
        
        foundHt = extractHtFromDict(screen)
        hashtags = getHashTags(screen.get("id", 0),foundHt)
        for el in screen['attributes']['components']:
            foradding = processComponent(el)
            addItTo(content_layout, foradding)

            # когда нужно посмотреть "широким взглядом" мы закомментируем предидущю строку и расскоментируем "ктулху"
            # if foradding:
            #   boxcontainer = MyBoxLayout(orientation='vertical', size_hint=(0.5, None), spacing=10, padding=(12,12))
            #   for i in range(5):
            #     button = MyButton(text=f'Button {i}', size_hint=(1, None), height=10, width=10, padding=(2,2))
            #     boxcontainer.add_widget(button)
            #     boxcontainer.do_layout()
            #   boxcontainer.do_layout()
            #   content_layout.add_widget(boxcontainer)
            #   content_layout.add_widget(foradding)

              
        self.add_widget(content_layout)    

        # scroll_view = ScrollView(size_hint=(1, 1))
        # scroll_view.add_widget(content_layout)
        # self.add_widget(scroll_view)
              
    
    
class TestApp(App):
    # def exitApp2(self):
    #     print('The button 2 is being pressed')
    #     exit() 
    
    def exitApp(self, instance):
        print('The Exit button <%s> is being pressed' % instance.text)
        exit()
        
    def build(self):
        if auth():
            dat = getScreens()
            if not dat:
                print('fail server!')
                # exit()
                # return False
            else:   
                if 'data' in dat:
                    screens = dat['data']
                    for screen in screens:
                        return  parseScreen(screen)
            
        btn2e = MyButton(text='some failed, exit')
        btn2e.bind(on_press=self.exitApp)
        return btn2e


if __name__ == '__main__':
    TestApp().run()

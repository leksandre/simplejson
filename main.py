import kivy
kivy.require('1.0.7')
from some import API_KEY, pgdb, pguser, pgpswd, pghost, pgport, pgschema, url_a, url_l, urlD, log_e, pass_e, managers_chats_id, service_chats_id, AppId, ObjectId, url_hash_objects, url_hash_filters_events,url_refresh
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.carousel import Carousel
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
    # store.delete(key)
        
def processHashtagData(data):
    for element in data:
        if 'type' in element:
            if 'id' in element:
                if 'attributes' in element:
                    attributes = element['attributes']
                    print('add'+element['type'],attributes)
                    
                    # store['hashtags_'+element['type']][element['type']] = {id:element['id'], **attributes}
                    
                    store.put('#'+(element['type']).lower()+'#', name=element['type'], id=element['id'], **attributes)

        else:
            if 'id' in element:
                if 'attributes' in element:
                    attributes = element['attributes']
                    if 'tag' in attributes:
                        # store['hashtags_'+attributes['tag']][attributes['tag']] = {data:attributes['data']}
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
    data = r.json()
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
    return True
    
def auth():
    global access_token
    global refresh_token
    
    if len(access_token)>0:
        return True
    
    PARAMS = {'login':log_e,'password':pass_e}
    url_e = urlD+(url_a.replace('userLogin555',log_e)).replace('userPassword888',pass_e)
    
    r = simpleRequest(isGet=True, url = url_e, params = PARAMS)
    data = r.json()
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
    return True

def processComponents(component, ui_components):
    if 'components' in component:
     for elemData in component['components']:
        # print('- ',elemData)
        if 1:
            foradding = processComponent(elemData)
            if foradding:
                ui_components[0].add_widget(foradding)
    
def draw_mbst_flexrow_col(component, size_hint = 0):
    print("component Col ['css']",component['css'])
    # if component.get('properties',None).get('backendname',None):
    #     print("component Col ['properties']['backendname']",component['properties']['backendname'])
    if size_hint!=0:
        elem = BoxLayout(orientation='vertical', size_hint=(size_hint, 1))
    else:
        elem = BoxLayout(orientation='vertical')
    processComponents(component,[elem])
    return elem
    
def draw_mbst_slider(component):
    print("component Slider ['css']",component['css'])
    elem = BoxLayout(orientation='vertical')
    processComponents(component,[elem])
    return elem
    
def processItems(component, ui_components):
    if 'items' in component:
      fullColWidth = 0  
      for elem in component['items']:
       if elem.get('properties',None).get('colwidth',None):
        fullColWidth += int(elem['properties']['colwidth'])
        
      for elem in component['items']: # если это стурктура с items
       curColWidth = 0 
    #    print('!!--aliasName',elem['aliasName'])
    #    print('!!--name',elem['name'])
       if elem.get('properties',None).get('colwidth',None):
        # print('!!--colwidth',elem['properties']['colwidth'])
        if fullColWidth>0:
            curColWidth = int(elem['properties']['colwidth'])/fullColWidth
    
       # варинат 1 отправляем в "конвейер", т.е. создаём "бокс" для каждого элемента из items и обрабатываем его содержимое соответственно "линейно", но без влияния на родительский компонент
       foradding = processComponent(elem, size_hint = curColWidth)
       if foradding:
        ui_components[0].add_widget(foradding)
        
       # вариант 2 сами реагируем на структуру компонента пропуская обработку элементов "обёрток" mbst-slider__slide mbst-flexrow__col
    #    if 'components' in elem:
    #     for elemData in elem['components']:
    #         # print('- ',elemData)
    #         if 1:
    #             foradding = processComponent(elemData)
    #             if foradding:
    #                 ui_components[0].add_widget(foradding)

                    
                    
def draw_mbst_slider(component): #has items!
    carousel = Carousel(direction='right')
    processItems(component,[carousel])
    # TabbedPanel #??????
    
    # if 'items' in component:
    #   for elem in component['items']:
    #    if 'components' in elem:
    #     for elemData in elem['components']:
    #         # print('- ',elemData)
    #         if 1:
    #             foradding = processComponent(elemData)
    #             if foradding:
    #                 carousel.add_widget(foradding)
                    
    return carousel

def draw_mbst_flexrow(component): #has items!
    layout = BoxLayout(orientation='horizontal',spacing=0) #, minimum_height=100
    processItems(component,[layout])
    
    # if 'items' in component:
    #   for elem in component['items']:
    #    if 'components' in elem:
    #     for elemData in elem['components']:
    #         # print('- ',elemData)
    #         if 1:
    #             foradding = processComponent(elemData)
    #             if foradding:
    #                 layout.add_widget(foradding)
                    
    # layout.add_widget(Button(text=f'layout_n'))
    return layout

def draw_mbst_video_player(component):
    # print("-component properties ['properties']['source'] ",component['properties']['source'])
    # player = VideoPlayer(source='myvideo.avi', state='play',options={'eos': 'loop'}) #VideoPlayerAnnotation
    player = VideoPlayer(source='myvideo.avi', state='play',options={'fit_mode': 'contain'})
    return player

def draw_mbst_button(component):
    # print("component Button ['css']",component['css'])
    btnSimple = Button(text=component['properties'].get('text', ""))
    # btn2e.bind(on_press=)
    # btn2e.bind(on_release=)
    return btnSimple

def draw_mbst_image(component):
    this_url = False
    if component.get('properties', None).get('image', None).get('url', None):
        try:
            this_url = component['properties']['image']['url']
            print("-------component properties ['properties']['image']'url' ", this_url)
        except KeyError as e:
            print(' KeyError  ' + str(e))
    else:    
     if component.get('properties', None).get('image', None).get('attributes', None).get('Url', None):
        try:
            this_url = component['properties']['image']['attributes']['Url']
            print("-------component properties ['properties']['image']['attributes']'url' ", this_url)
        except KeyError as e:
            print(' KeyError  ' + str(e))
        
    # if component.get('properties', None).get('backendname', None):
    #     bn = component['properties']['backendname']
    #     if bn == 'Image-384508c6':
    #         print("component image ['properties']['backendname']",bn)
    #         print(component['properties']['image']['attributes']['Url'])
        
    # wimg = Image(source='mylogo.png')
    # aimg = AsyncImage(source='https://viafdn-admin.mobsted.com/tenants/viafdn/uploads/2021/7/20/20095bc04ac1dfe4b3337d10caa77ca9.png')
    
    if this_url:
        aimg = AsyncImage(source=this_url)
        return aimg
    return False
    
def draw_mbst_text(component):
    textinput = Label(text=component['properties'].get('text', ""))
    # btn2e.bind(on_ref_press=)
    return textinput
    
def draw_mbst_text_area(component):
    textinput = TextInput(text=component['properties'].get('text', ""), multiline=True)
    # textinput.bind(on_text_validate=on_enter)
    # textinput.bind(text=on_text)
    return textinput

def draw_mbst_link(component):
    # widget = Label(text='Hello [ref=world]World[/ref]', markup=True)
    widget = Label(text=component['properties'].get('text', ""), markup=True)
    # widget.bind(on_ref_press=print_it)
    return widget

def processHtOnComponent(component):
    
    text = json.dumps(component)
    ht = extractHtFromDict(text)
    
    for h in ht:
        # print('ht --',h)
        p_ht = h.split(':')
        if len(p_ht)>1:
            if store.exists('#'+p_ht[0].lower()+'#'):
                ht_v = store.get('#'+p_ht[0].lower()+'#')
                if p_ht[1] in ht_v:
                    # print(h,'=>',p_ht[1],'=>',ht_v.get(p_ht[1]))
                    text = text.replace('#'+h+'#',ht_v.get(p_ht[1]))

    try:
        componentNew = json.loads(text)
        if componentNew:
            # print(' ret new compotetn  ')
            return componentNew                
    except KeyError as e:
        print(' not json as text KeyError  ' + str(e))
                

    return component
    
def processComponent(component, size_hint = 0):

    # for elem in component:
    #     print('-component',elem)
    # print('-component properties',component['properties'])
        
    el = component
    
    # print('css',el['css'])
    # print('config',el['config'])
    
    el = processHtOnComponent(el)#заменяем хештеги

        
    # отрисовываем компоненты и возврщаем их вызвавшему родительскому компоненту
    if el['name'] == 'mbst-flexrow':
        return draw_mbst_flexrow(el)
    if el['name'] == 'mbst-slider':
        return draw_mbst_slider(el)
    # подэлементы от flexrow и slider
    if el['name'] == 'mbst-flexrow__col':
        return draw_mbst_flexrow_col(el, size_hint)
    if el['name'] == 'mbst-slider__slide':
        return draw_mbst_flexrow_col(el) 


    if 'items' in component:
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
    

    
    
    print('!-aliasName',el['aliasName'])
    print('!-name',el['name'])
    return False



                     
            

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
        print('len(data)',len(r.text))
        if not 'data' in data:
            print(' not data 1 ' + str(data))
            return False
        processHashtagData(data['data'])


    # store.put('hashtags', name='Object', org='kivy')
    # store['hashtags'] = {'name': 'Mathieu'}
    # hashtags.append
    
    
    eventsFilterHt = list(filter(lambda x: x.lower().startswith('eventsfilter:'), ht))
    if len(objectHt)>0:
        fullHt = [ {"tag": "#"+str(x)+"#", "objectId": ObjectId, "pagination": {"page": 1, "pageSize": 10, "showButtonUp": False, "showInformer": True}} for x in eventsFilterHt]
        
        json_details = {"applicationId": AppId, "objectId": ObjectId, "extraParams": {"Screen": {
            "id": screenId}, "Globals": {"applicationId": AppId, "objectId": ObjectId}}, "tags": fullHt}

        maindata =  json.dumps(json_details) 
        
        r = simpleRequest(url = urlD+url_hash_filters_events, headers=Headers, data=maindata)  # example of body  --data-raw '{"applicationId":18,"objectId":500,"extraParams":{"Tenant":{},"Application":{},"Screen":{"id":49,"ApplicationId":18,"SortOrder":0,"Name":"Home screen","UpdateDate":"2021-05-19 08:11:18.695368","CreateDate":"2021-05-19 08:11:18.695368","uuid":"ba1db960-178a-410c-833a-0d675e1e296b","LastModified":"2024-01-12 07:31:04.286629","ishomescreen":True,"name":"mbst-screen","aliasName":"Screen"},"Object":{"FirstName":"Aleksandr I","CompanyAccount":"0","Image":"https://viafdn-admin.mobsted.com/tenants/viafdn/uploads/2021/7/7/6361866df06e28611bb3a3e8bea8d15f.png","FacebookChannel":null,"ChromePush":null,"Points":"0","Range":"The Helpful Citizen"},"Variable":{"MenuMS":"0","MenuR":"0","MenuMKL":"0","ShowEdit":"0","HeartPopup":"20240122","PushWidget":"on"},"Payment":{},"Backendname":{"EditAct2#Loop:GD:backend@id#":"#Loop:GD:backend@ext_col_json:Message#"},"LastEvent":{},"Route":{"path":"/18/","query":{"appid":"18","screenid":"49","objid":"500","os":"ios"},"params":{"appid":"18"}},"Tax":{},"Globals":{"applicationId":18,"objectId":500}},"tags":[{"tag":"#EventsFilter:MyGD:Data#","objectId":500,"pagination":{"page":1,"pageSize":10,"showButtonUp":False,"showInformer":False}},{"tag":"#EventsFilter:GD:Data#","objectId":500,"pagination":{"page":1,"pageSize":10,"showButtonUp":False,"showInformer":True}}]}'
        
        if not r:
            return {}

        # print(r)
        data = r.json()
        print(r.text[0:200])
        print('len(data)',len(r.text))
        if not 'data' in data:
            print(' not data 1 ' + str(data))
            return False
        processHashtagData(data['data'])
    
    return {}
    
    
def filterTags(x):
    if x.lower().startswith('loop:'):
        return False
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
    # print('text screen',text[:400])
    foundHt = []
    try:
        found = re.findall(r'\#([\w:@]*)\#', text)
        found = list(set(found))
        foundHt = list(filter(lambda x: filterTags(x), found))
    except AttributeError:
        pass
    if foundHt:
        print('found', foundHt)
    return foundHt
      
def parseScreen(screen):
    layoutScreen = GridLayout(cols=1, spacing=0)# , size_hint_y=2
    
    # layoutScreen = GridLayout(cols=1, spacing=10, size_hint_y=None)
    # layoutScreen.bind(minimum_height=layoutScreen.setter('height'))
    root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
    
    foundHt = extractHtFromDict(screen)

    hashtags = getHashTags(screen.get("id", 0),foundHt)
    for el in screen['attributes']['components']:
        foradding = processComponent(el)
        if foradding:
            layoutScreen.add_widget(foradding)
    

    root.add_widget(layoutScreen)
    return root
        

       
    
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
            screens = dat['data']
            for screen in screens:
                return  parseScreen(screen)
            
        btn2e = Button(text='some failed, exit')
        btn2e.bind(on_press=self.exitApp)
        return btn2e


if __name__ == '__main__':
    TestApp().run()

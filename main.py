import kivy
kivy.require('1.0.7')
from some import API_KEY, pgdb, pguser, pgpswd, pghost, pgport, pgschema, url_a, url_l, urlD, log_e, pass_e, managers_chats_id, service_chats_id, AppId, ObjectId, url_hash_objects, url_hash_filters_events
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

store = JsonStore(f'appid_{AppId}_objid_{ObjectId}')

hashtags = []

if store.exists('hashtags'):
    hashtagsS =  store.get('hashtags')
    print('-------------- hashtags exists:', hashtagsS)
    hashtags = list(hashtagsS)
    # store.delete('hashtags')

    
    
from kivy.config import Config
Config.set('graphics', 'width', '100')
Config.set('graphics', 'height', '200')

from kivy.core.window import Window
Window.size = (600, 1000)

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

# config 
execution_path = os.getcwd()


global access_token
access_token = ''

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

def auth():
    global access_token
    
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
        # print('tokens - ',data,access_token,refresh_token)
    except KeyError as e:
        print('!!! over KeyError 43 ' + str(e))
        return False
    return True

def draw_mbst_slider(component):
    carousel = Carousel(direction='right')
    # TabbedPanel #??????
    
    if 'items' in component:
      for elem in component['items']:
       if 'components' in elem:
        for elemData in elem['components']:
            # print('- ',elemData)
            if 1:
                foradding = processComponent(elemData)
                if foradding:
                    carousel.add_widget(foradding)
                    
    return carousel


def draw_mbst_video_player(component):
    # print("-component properties ['properties']['source'] ",component['properties']['source'])
    # player = VideoPlayer(source='myvideo.avi', state='play',options={'eos': 'loop'}) #VideoPlayerAnnotation
    player = VideoPlayer(source='myvideo.avi', state='play',options={'fit_mode': 'contain'})
    return player

def draw_mbst_button(component):
    btnSimple = Button(text=component['properties'].get('text', ""))
    # btn2e.bind(on_press=)
    # btn2e.bind(on_release=)
    return btnSimple

def draw_mbst_image(component):
    # print("-component properties ['properties']['image']'url' ",component['properties']['image']['url'])
    # wimg = Image(source='mylogo.png')
    aimg = AsyncImage(source='https://viafdn-admin.mobsted.com/tenants/viafdn/uploads/2021/7/20/20095bc04ac1dfe4b3337d10caa77ca9.png')
    return aimg
    
def draw_mbst_text(component):
    textinput = TextInput(text=component['properties'].get('text', ""), multiline=False)
    # btn2e.bind(focus=)
    # btn2e.bind(insert_text=)
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
    
def draw_mbst_flexrow(component):
    layout = BoxLayout(orientation='vertical',spacing=10)
    
    if 'items' in component:
      for elem in component['items']:
       if 'components' in elem:
        for elemData in elem['components']:
            # print('- ',elemData)
            if 1:
                foradding = processComponent(elemData)
                if foradding:
                    layout.add_widget(foradding)
                    
    # layout.add_widget(Button(text=f'layout_n'))
    return layout

def processComponent(component):

    # for elem in component:
    #     print('-component',elem)
    # print('-component properties',component['properties'])
        
    el = component
    # print('css',el['css'])
    # print('config',el['config'])
    
    
        
    if el['name'] == 'mbst-flexrow':
        return draw_mbst_flexrow(el)
    if el['name'] == 'mbst-slider':
        return draw_mbst_slider(el)
        
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

    
    print('name',el['name'])
    return False



def getHashTags(screenId):
    if screenId==0:
        return {}
    Headers = { 'Authorization' : "Bearer "+str(access_token), 'Content-Type':"application/json" }
    json_details = {
        "applicationId": "18",
        "ids": [500],
        "tags":["#Object:FirstName#","#Object:CompanyAccount#","#Object:Image#"]
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

    for object in data['data']:
        attributes = object['attributes']
        store.put('hashtags', name='Object', id=object['id'], **attributes)
    # store.put('hashtags', name='Object', org='kivy')
    # store['hashtags'] = {'name': 'Mathieu'}
    # hashtags.append
    
    json_details = {"applicationId": 18, "objectId": 500, "extraParams": {"Screen": {"id": 49}, "Globals": {"applicationId": 18, "objectId": 500}}, "tags": [{"tag": "#EventsFilter:MyGD:Data#", "objectId": 500, "pagination": {"page": 1, "pageSize": 10, "showButtonUp": False, "showInformer": False}}, {"tag": "#EventsFilter:GD:Data#", "objectId": 500, "pagination": {"page": 1, "pageSize": 10, "showButtonUp": False, "showInformer": True}}]}
    
    maindata =  json.dumps(json_details) 
    
    r = simpleRequest(url = urlD+url_hash_filters_events, headers=Headers, data=maindata)  # example of body  --data-raw '{"applicationId":18,"objectId":500,"extraParams":{"Tenant":{},"Application":{},"Screen":{"id":49,"ApplicationId":18,"SortOrder":0,"Name":"Home screen","UpdateDate":"2021-05-19 08:11:18.695368","CreateDate":"2021-05-19 08:11:18.695368","uuid":"ba1db960-178a-410c-833a-0d675e1e296b","LastModified":"2024-01-12 07:31:04.286629","ishomescreen":True,"name":"mbst-screen","aliasName":"Screen"},"Object":{"FirstName":"Aleksandr I","CompanyAccount":"0","Image":"https://viafdn-admin.mobsted.com/tenants/viafdn/uploads/2021/7/7/6361866df06e28611bb3a3e8bea8d15f.png","FacebookChannel":null,"ChromePush":null,"Points":"0","Range":"The Helpful Citizen"},"Variable":{"MenuMS":"0","MenuR":"0","MenuMKL":"0","ShowEdit":"0","HeartPopup":"20240122","PushWidget":"on"},"Payment":{},"Backendname":{"EditAct2#Loop:GD:backend@id#":"#Loop:GD:backend@ext_col_json:Message#"},"LastEvent":{},"Route":{"path":"/18/","query":{"appid":"18","screenid":"49","objid":"500","os":"ios"},"params":{"appid":"18"}},"Tax":{},"Globals":{"applicationId":18,"objectId":500}},"tags":[{"tag":"#EventsFilter:MyGD:Data#","objectId":500,"pagination":{"page":1,"pageSize":10,"showButtonUp":False,"showInformer":False}},{"tag":"#EventsFilter:GD:Data#","objectId":500,"pagination":{"page":1,"pageSize":10,"showButtonUp":False,"showInformer":True}}]}'
    
    if not r:
        return {}

    # print(r)
    data = r.json()
    print(r.text[0:200])
    print('len(data)',len(r.text))
    
    return {}
    
    


  
def parseScreen(screen):
    layoutScreen = GridLayout(cols=1)
    hashtags = getHashTags(screen.get("id", 0))
    for el in screen['attributes']['components']:
        foradding = processComponent(el)
        if foradding:
            layoutScreen.add_widget(foradding)
            
    # layoutScreen.add_widget(BoxLayout(orientation='vertical'))
    # btn2e = Button(text='exit')
    # btn2e.bind(on_press=TestApp().exitApp2())
    # layoutScreen.add_widget(btn2e)
    return layoutScreen
        

       
    
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

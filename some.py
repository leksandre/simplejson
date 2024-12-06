API_KEY='6730373982:AAHDXANvVcgifs6G_I-9tRAWC8_Oxs9B_yc'  # change this to the token you get from @BotFather
CHATfortest='526602346'  # can be a @username or a id, change this to your own @username or id for example.
pgdb = 'domotel'
pguser = 'postgres'
pgpswd = 'postgres'
pghost = 'localhost'
pgport = '6432'
pgschema = 'domotel'
log_e = 'xxx'
pass_e = 'login1'
url_a = 'api/v8/auth?login=userLogin555&password=userPassword888'
url_refresh = 'api/v8/refresh?refresh_token=ref_token'
url_l = 'api/v8/screen'
url_hash_filters_events = 'api/v8/hashtags/filters/events'
url_hash_objects = 'api/v8/hashtags/objects'
service_chats_id = ['526602346']
managers_chats_id = ['526602346']


donotprocessstyles = False

import random
import sys

arguments = sys.argv
print('-----arguments',arguments)
# if(random.randint(1, 99) > 50) or len(arguments)>1:
if len(arguments)>1:
    urlD = 'https://viafdn-admin.mobsted.com/'
    AppId = 18
    ObjectId = 500
    if arguments[1]=='offstyle=1':
        donotprocessstyles = True
else:
    urlD = 'https://test-admin.mobsted.ru/'
    AppId = 34
    ObjectId = 3441

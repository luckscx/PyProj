
from weibo import APIClient


APP_KEY = '2962578590' # app key
APP_SECRET = '59e66c610b90bde1fa65fef873334f16' # app secret
CALLBACK_URL = 'https://api.weibo.com/oauth2/default.html' # callback url

client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)

code="04eaa5518f0d3c4208251848b4caaf50"
r = client.request_access_token(code)
access_token = r.access_token 
expires_in = r.expires_in 
print expires_in
client.set_access_token(access_token, expires_in)

r = client.statuses.user_timeline.get()
for st in r.statuses:
    print st.text
    

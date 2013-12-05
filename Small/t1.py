#coding=utf-8
from urllib import request
import re
import os


def Gethtml(url):
    content=request.urlopen(url,timeout=10).read()
    content = content.decode('utf-8')
    return content

def MakeDir(dir_name):
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)


def GetPicUrl(url):
    content=Gethtml(url);
    matchstr=r'http://wow.zamimg.com/images/hearthstone/cards/enus/original/.*?.png'   
    image_url=re.search(matchstr,content)
    return image_url.group()

picdir=r"pic"
MakeDir(picdir)
url="http://www.hearthhead.com/mechanic=11/secret#usedby:0+4+1"
url=re.sub(r'[\?\#].*$', '', url)


content=Gethtml(url)

image_ids = re.findall(r'"image":"(.*?)"', content)

card_ids = re.findall(r'"id":(\d{3,4}),', content)  

card_names=re.findall(r'\d,"name":"(.*?)","des',content)

pic_head=r"http://wow.zamimg.com/images/hearthstone/cards/enus/original/"

if len(image_ids) == len(card_names):
    for index,id in enumerate(image_ids):
        pic_url=pic_head+id+".png"
        picname=card_names[index]+".png"
        try:
            f = open(os.path.join(picdir,picname),"wb")
            f.write(request.urlopen(pic_url).read())
            f.close()
            print("save pic %s done!" % picname )
        except Exception:
            print("save pic %s error!" % picname)    

    
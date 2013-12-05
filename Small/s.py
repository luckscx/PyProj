#!/usr/bin/env python
# -*- coding: utf-8 -*-

import win32com.client 
import os

# 载入WORD模块
w = win32com.client.Dispatch("Word.Application")

# 后台运行，不显示，不警告
w.Visible = 0
w.DisplayAlerts = 0

oldstr= '嘉兴鸿翔新型建材有限公司'
newstr= '浙江鸿翔新材料科技有限公司'
wordfiletype= ('.doc','.docx','.txt')

#检查是否为临时word文件
def check(name):
    head=name[0:2]
    if head==r'~$':
        return True
    else:
        return False


def Test2(rootDir,modDir): 
    for lists in os.listdir(rootDir): 
        path = os.path.join(rootDir, lists)
        modpath= os.path.join(modDir, lists)
        houzhui=os.path.splitext(path)[1]

        #是文件打开操作
        if os.path.isfile(path):
            if check(lists):
                continue
            if houzhui in wordfiletype:  #判断是word文件
                w = win32com.client.Dispatch('Word.Application')  
                w.Visible = 0 
                w.DisplayAlerts = 0 
                orf = path      #准备替换的文件
                thf = modpath   #替换完成后输出的文件
                
                doc = w.Documents.Open( FileName = orf )
                
                w.Selection.Find.ClearFormatting()
                w.Selection.Find.Replacement.ClearFormatting()

                w.Selection.Find.Execute(oldstr, False, False, False, False, False, True, 1, True,newstr, 2)

                w.ActiveDocument.Sections[0].Headers[0].Range.Find.ClearFormatting()
                w.ActiveDocument.Sections[0].Headers[0].Range.Find.Replacement.ClearFormatting()
                w.ActiveDocument.Sections[0].Headers[0].Range.Find.Execute(oldstr[0], False, False, False, False, False, True, 1, False, newstr[0] , 2)
                
                doc.SaveAs(thf)
                doc.Close()
                print(orf,' 替换完成')
            else:
                if not os.path.exists(modpath) or(os.path.exists(modpath) and (os.path.getsize(modpath) != os.path.getsize(path))):  
                    open(modpath, "wb").write(open(path, "rb").read())
                    print(path,' 为非word文件，纯拷贝')
                

        #文件夹则创建
        if os.path.isdir(path):
            if not os.path.exists(modpath):
                os.mkdir(modpath) 
            Test2(path,modpath) 

if __name__=='__main__':
    Test2(r'd:\b1',r'd:\b2')
    w.Quit()


# -*- coding: utf-8 -*-
import random
import string

word_len=input("请输入密码串长度:")

guess_list=[]
if word_len.isdigit():
    word_len=int(word_len)
    ans_str="".join(random.sample(string.ascii_lowercase,word_len))
    guess_list=['*' for i in range(word_len)]

hit=0
while hit<word_len:
    print("".join(guess_list))
    b=input("你猜个字母看看？")
    b=b[0].lower()
    count=ans_str.count(b)
    if count==0:
        print("没有 %s 哦" % b)
    else:
        index=0
        for i in range(count):
            index=ans_str.find(b,index)
            guess_list[index]=ans_str[index]
            hit+=1    
        
print("".join(guess_list))
print("你都猜对了，好棒！")
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,s

def a(root):
    for lists in os.listdir(root):
        path=os.path.join(root,lists)
        if os.path.isfile(path):
            if s.check(lists):
                os.remove(path)
        if os.path.isdir(path):
            a(path)

if __name__=='__main__':
    a(r'd:\D')

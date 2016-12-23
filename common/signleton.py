#!/usr/bin/python
#-*- coding:utf-8 -*-

def signleton(cls, *args, **kw):
    instances = {}
    def _signleton(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return  _signleton

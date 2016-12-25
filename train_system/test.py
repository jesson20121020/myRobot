#coding:utf-8
import os

def execCmd(cmd):
    r = os.popen(cmd)
    text = r.read()
    r.close()
    return text


print execCmd('python tickets.py -g 上海 西安 2016-12-28')

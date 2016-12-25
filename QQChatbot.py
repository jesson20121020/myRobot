#coding:utf-8

from qqbot import QQBot

class MyQQBot(QQBot):
    def onPollComplete(self, msgType, from_uin, buddy_uin, message):
        # if message == '-hello':
        #     self.send(msgType, from_uin, '你好，我是QQ机器人')
        # elif message == '-stop':
        #     self.stopped = True
        #     self.send(msgType, from_uin, 'QQ机器人已关闭')
        import AutoReplyMgr
        reply = AutoReplyMgr.instance().auto_reply(str(from_uin), message)
        self.send(msgType, from_uin, reply)

myqqbot = MyQQBot()
myqqbot.Login()
myqqbot.Run()


class MyQQBot2(object):
    def __init__(self):
        self.x = 0

    def test2(self):
        pass

    def test3(self):
        self.x = 0
    
    def test4(self):
        import os
        os.getcwd()

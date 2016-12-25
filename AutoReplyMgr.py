#coding:utf-8

import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')

_instance = None
def instance():
	global _instance
	if _instance == None:
		_instance = AutoReplyMgr()
	return _instance

class AutoReplyMgr(object):
	def __init__(self):
		pass

	def auto_reply(self, uid, msg):
		# 优先由特殊服务管理器处理消息
		import SpecialServiceMgr
		status, result = SpecialServiceMgr.handle_msg(msg)
		if status: return result
		import ChatServiceMgr
		status, result = ChatServiceMgr.handle_msg(uid, msg)
		if result: return result


# print instance().auto_reply('1233', u'翻译你好啊')
# print instance().auto_reply('1233', u'翻译 hello, how are you')
# print instance().auto_reply('1233', u'hello, how are you')
print instance().auto_reply('1233', u'111')


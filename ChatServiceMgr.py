#coding:utf-8
import Utils
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def handle_msg(uid, msg):
	return instance().handle_msg(uid, msg)

_instance = None
def instance():
	global _instance
	if _instance == None:
		_instance = ChatServiceMgr()
	return _instance

# 聊天服务管理
class ChatServiceMgr(object):
	def __init__(self):
		pass

	def handle_msg(self, uid, msg):
		if Utils.is_chinese(msg) or Utils.is_number(msg):
			import TulingAutoReply
			return TulingAutoReply.instance().respond(uid, msg)
		else:
			import AliceAutoReply
			return AliceAutoReply.instance().respond(uid, msg)



# print instance().handle_msg('123', u'你好啊')[1]
# print instance().handle_msg('123', u'1111')

# print Utils.is_number(u'1111')









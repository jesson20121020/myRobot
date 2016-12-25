#coding:utf-8

# 自动回复基类
class AutoReplyBase(object):
	def __init__(self):
		pass

	def respond(self, uid, msg):
		return False, ''

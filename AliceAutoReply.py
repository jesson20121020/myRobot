#coding:utf-8
import aiml
import os
import AutoReplyBase

_instance = None
def instance():
	global _instance
	if _instance == None:
		_instance = AliceAutoReply()
	return _instance

# 英文自动回复提供方 Alice
class AliceAutoReply(AutoReplyBase.AutoReplyBase):
	def __init__(self):
		super(AliceAutoReply, self).__init__()
		cur_dir = os.getcwd()
		os.chdir('./alice')
		self.alice = aiml.Kernel()
		self.alice.setBotPredicate("name", "Alice")
		self.alice.learn("startup.xml")
		a = self.alice.respond('LOAD ALICE')
		os.chdir(cur_dir)

	def respond(self, uid, msg):
		result = self.alice.respond(msg)
		print '    ROBOT:', result
		return True, result


# print instance().respond('', 'hello')

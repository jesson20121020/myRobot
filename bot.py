#!/usr/bin/env python
# coding: utf-8

from wxbot import *
import json
import math


DEFAULT_WX_ROBOT_SWITCH = True

class WXChatbot(WXBot):
	def __init__(self):
		WXBot.__init__(self)
		self.robot_switch = DEFAULT_WX_ROBOT_SWITCH

	def auto_switch(self, msg):
		msg_data = msg['content']['data']
		stop_cmd = [u'退下', u'走开', u'关闭', u'关掉', u'休息', u'滚开']
		start_cmd = [u'出来', u'启动', u'工作']
		if self.robot_switch:
			if msg_data in stop_cmd:
				self.robot_switch = False
				self.send_msg_by_uid(u'再见，记得想我哦！', msg['to_user_id'])
		else:
			if msg_data in start_cmd:
				self.robot_switch = True
				self.send_msg_by_uid(u'我是可爱的小冰轩，我会得可多了！', msg['to_user_id'])

	def handle_msg_all(self, msg):
		if not self.robot_switch: return
		import AutoReplyMgr
		# print 'xdc:::::msg:::', self.robot_switch, msg
		# if not self.robot_switch and msg['msg_type_id'] != 1:
		#	  return
		# print 'xdc:::::::::', msg
		if msg['msg_type_id'] == 1 and msg['content']['type'] == 0:  # reply to self
			self.auto_switch(msg)

		elif msg['msg_type_id'] == 4 and msg['content']['type'] == 0:  # text message from contact
			reply = AutoReplyMgr.instance().auto_reply(msg['user']['id'], msg['content']['data'])
			if reply:
				self.send_msg_by_uid(reply, msg['user']['id'])
			self.send_img_msg_by_uid('img/1.png', msg['user']['id'])
			self.send_file_msg_by_uid('bot.py', msg['user']['id'])

		elif msg['msg_type_id'] == 4 and msg['content']['type'] == 0:  # text message from contact
			reply = AutoReplyMgr.instance().auto_reply(msg['user']['id'], msg['content']['data'])
			if reply:
				self.send_msg_by_uid(reply, msg['user']['id'])

		elif msg['msg_type_id'] == 3 and msg['content']['type'] == 0:  # group text message
			self.auto_switch(msg)
			if not self.robot_switch:
				return
			if 'detail' in msg['content']:
				my_names = self.get_group_member_name(self.my_account['UserName'], msg['user']['id'])
				if my_names is None:
					my_names = {}
				if 'NickName' in self.my_account and self.my_account['NickName']:
					my_names['nickname2'] = self.my_account['NickName']
				if 'RemarkName' in self.my_account and self.my_account['RemarkName']:
					my_names['remark_name2'] = self.my_account['RemarkName']

				is_at_me = False
				for detail in msg['content']['detail']:
					if detail['type'] == 'at':
						for k in my_names:
							if my_names[k] and my_names[k] == detail['value']:
								is_at_me = True
								break
				if is_at_me:
					src_name = msg['content']['user']['name']
					reply = 'to ' + src_name + ': '
					if msg['content']['type'] == 0:  # text message
						reply += AutoReplyMgr.instance().auto_reply(msg['content']['user']['id'], msg['content']['desc'])
					else:
						reply += u"对不起，只认字，其他杂七杂八的我都不认识，,,Ծ‸Ծ,,"
					self.send_msg_by_uid(reply, msg['user']['id'])
				else:
					reply = AutoReplyMgr.instance().auto_reply(msg['content']['user']['id'], msg['content']['desc'])
					self.send_msg_by_uid(reply, msg['user']['id'])

			else:
				reply = AutoReplyMgr.instance().auto_reply(msg['content']['user']['id'], msg['content']['desc'])
				self.send_msg_by_uid(reply, msg['user']['id'])





# class TulingWXBot(WXBot):
#	def __init__(self):
#		WXBot.__init__(self)
#		self.tuling_key = ""
#		self.robot_switch = True

#	def auto_switch(self, msg):
#		msg_data = msg['content']['data']
#		stop_cmd = [u'退下', u'走开', u'关闭', u'关掉', u'休息', u'滚开']
#		start_cmd = [u'出来', u'启动', u'工作']
#		if self.robot_switch:
#			for i in stop_cmd:
#				if i == msg_data:
#					self.robot_switch = False
#					self.send_msg_by_uid(u'[Robot]' + u'bye, remember miss me！', msg['to_user_id'])
#		else:
#			for i in start_cmd:
#				if i == msg_data:
#					self.robot_switch = True
#					self.send_msg_by_uid(u'[Robot]' + u'I am comming！', msg['to_user_id'])

#	def handle_msg_all(self, msg):
#		# print 'xdc:::::msg:::', self.robot_switch, msg
#		# if not self.robot_switch and msg['msg_type_id'] != 1:
#		#	  return

		elif msg['msg_type_id'] == 3 and msg['content']['type'] == 0:  # group text message
			self.auto_switch(msg)
			if not self.robot_switch:
				return
			if 'detail' in msg['content']:
				my_names = self.get_group_member_name(self.my_account['UserName'], msg['user']['id'])
				if my_names is None:
					my_names = {}
				if 'NickName' in self.my_account and self.my_account['NickName']:
					my_names['nickname2'] = self.my_account['NickName']
				if 'RemarkName' in self.my_account and self.my_account['RemarkName']:
					my_names['remark_name2'] = self.my_account['RemarkName']

				is_at_me = False
				for detail in msg['content']['detail']:
					if detail['type'] == 'at':
						for k in my_names:
							if my_names[k] and my_names[k] == detail['value']:
								is_at_me = True
								break
				if is_at_me:
					src_name = msg['content']['user']['name']
					reply = 'to ' + src_name + ': '
					if msg['content']['type'] == 0:  # text message
						reply += AutoReplyMgr.instance().auto_reply(msg['content']['user']['id'], msg['content']['desc'])
					else:
						reply += u"对不起，只认字，其他杂七杂八的我都不认识，,,Ծ‸Ծ,,"
					self.send_msg_by_uid(reply, msg['user']['id'])
				else:
					reply = AutoReplyMgr.instance().auto_reply(msg['content']['user']['id'], msg['content']['desc'])
					self.send_msg_by_uid(reply, msg['user']['id'])

			else:
				reply = AutoReplyMgr.instance().auto_reply(msg['content']['user']['id'], msg['content']['desc'])
				self.send_msg_by_uid(reply, msg['user']['id'])





# class TulingWXBot(WXBot):
#	def __init__(self):
#		WXBot.__init__(self)
#		self.tuling_key = ""
#		self.robot_switch = True

#	def auto_switch(self, msg):
#		msg_data = msg['content']['data']
#		stop_cmd = [u'退下', u'走开', u'关闭', u'关掉', u'休息', u'滚开']
#		start_cmd = [u'出来', u'启动', u'工作']
#		if self.robot_switch:
#			for i in stop_cmd:
#				if i == msg_data:
#					self.robot_switch = False
#					self.send_msg_by_uid(u'[Robot]' + u'bye, remember miss me！', msg['to_user_id'])
#		else:
#			for i in start_cmd:
#				if i == msg_data:
#					self.robot_switch = True
#					self.send_msg_by_uid(u'[Robot]' + u'I am comming！', msg['to_user_id'])

#	def handle_msg_all(self, msg):
#		# print 'xdc:::::msg:::', self.robot_switch, msg
#		# if not self.robot_switch and msg['msg_type_id'] != 1:
#		#	  return
#		# print 'xdc:::::::::', msg
#		if msg['msg_type_id'] == 1 and msg['content']['type'] == 0:  # reply to self
#			self.auto_switch(msg)
#		elif msg['msg_type_id'] == 4 and msg['content']['type'] == 0:  # text message from contact
#			self.send_msg_by_uid(self.tuling_auto_reply(msg['user']['id'], msg['content']['data']), msg['user']['id'])
#		elif msg['msg_type_id'] == 3 and msg['content']['type'] == 0:  # group text message
#			self.auto_switch(msg)
#			if not self.robot_switch:
#				return
#			if 'detail' in msg['content']:
#				my_names = self.get_group_member_name(self.my_account['UserName'], msg['user']['id'])
#				if my_names is None:
#					my_names = {}
#				if 'NickName' in self.my_account and self.my_account['NickName']:
#					my_names['nickname2'] = self.my_account['NickName']
#				if 'RemarkName' in self.my_account and self.my_account['RemarkName']:
#					my_names['remark_name2'] = self.my_account['RemarkName']

#				is_at_me = False
#				for detail in msg['content']['detail']:
#					if detail['type'] == 'at':
#						for k in my_names:
#							if my_names[k] and my_names[k] == detail['value']:
#								is_at_me = True
#								break
#				if is_at_me:
#					src_name = msg['content']['user']['name']
#					reply = 'to ' + src_name + ': '
#					if msg['content']['type'] == 0:  # text message
#						reply += self.tuling_auto_reply(msg['content']['user']['id'], msg['content']['desc'])
#					else:
#						reply += u"对不起，只认字，其他杂七杂八的我都不认识，,,Ծ‸Ծ,,"
#					self.send_msg_by_uid(reply, msg['user']['id'])
#				else:
#					reply = self.tuling_auto_reply(msg['content']['user']['id'], msg['content']['desc'])
#					self.send_msg_by_uid(reply, msg['user']['id'])

#			else:
#				reply = self.tuling_auto_reply(msg['content']['user']['id'], msg['content']['desc'])
#				self.send_msg_by_uid(reply, msg['user']['id'])


def main():
	bot = WXChatbot()
	bot.DEBUG = True
	bot.conf['qr'] = 'png'

	bot.run()


def rpyc_server():
	from rpycserver import remote_call_func
	from rpyc.utils.server import ThreadedServer
	rpycServer = ThreadedServer(remote_call_func, hostname='localhost', port=11111, auto_register=False)
	rpycServer.start()
	print 'xdc::::::::::11'

if __name__ == '__main__':
	# thread.start_new_thread(main, ()) 
	# thread.start_new_thread(rpyc_server, ()) 
	# rpyc_server()
	# main()
	import threading
	t1 = threading.Thread(target = main, args=())
	t2 = threading.Thread(target = rpyc_server, args=())
	t1.setDaemon(True)
	t1.start()
	t2.setDaemon(True)
	t2.start()

	t2.join()


	

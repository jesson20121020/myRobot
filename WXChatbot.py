#!/usr/bin/env python
# coding: utf-8

from wxbot import *
import ConfigParser
import json
from BaiduTranslate import BaiduTranslate

import aiml
import os

def is_chinese(uchar):
	"""判断一个unicode是否是汉字"""
	if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
		return True
	else:
		return False

class Alice(object):
	def __init__(self):
		cur_dir = os.getcwd()
		os.chdir('./alice')
		self.alice = aiml.Kernel()
		self.alice.setBotPredicate("name", "Alice")
		self.alice.learn("startup.xml")
		a = self.alice.respond('LOAD ALICE')
		os.chdir(cur_dir)

	def respond(self, msg):
		return self.alice.respond(msg)

alice = Alice()
baidu_trans = BaiduTranslate()

class TulingWXBot(WXBot):
	def __init__(self):
		WXBot.__init__(self)

		self.tuling_key = ""
		self.robot_switch = True

		try:
			cf = ConfigParser.ConfigParser()
			cf.read('conf.ini')
			self.tuling_key = cf.get('main', 'key')
		except Exception:
			pass
		print 'tuling_key:', self.tuling_key

	def tuling_auto_reply(self, uid, msg):
		if len(msg) > 3 and msg[0:2] == u'翻译':
			srt = msg[2:].strip().encode('utf-8')
			is_ch = is_chinese(srt)
			from_lan = ['en', 'zh'][is_ch]
			to_lan = ['zh', 'en'][is_ch]
			dst = baidu_trans.translate(from_lan, to_lan, srt)
			if dst:
				return u'翻译结果:\n' + dst
		if self.tuling_key:
			url = "http://www.tuling123.com/openapi/api"
			user_id = uid.replace('@', '')[:30]
			body = {'key': self.tuling_key, 'info': msg.encode('utf8'), 'userid': user_id}
			r = requests.post(url, data=body)
			respond = json.loads(r.text)
			result = ''
			if respond['code'] == 100000:
				result = respond['text'].replace('<br>', '  ')
			elif respond['code'] == 200000:
				result = respond['url']
			elif respond['code'] == 302000:
				for k in respond['list']:
					result = result + u"【" + k['source'] + u"】 " +\
						k['article'] + "\t" + k['detailurl'] + "\n"
			else:
				result = respond['text'].replace('<br>', '  ')

			if u'我不会说英语的啦' in result:
				result = alice.respond(msg)

			print '    ROBOT:', result
			return result
		else:
			return u"知道啦"

	def auto_switch(self, msg):
		msg_data = msg['content']['data']
		stop_cmd = [u'退下', u'走开', u'关闭', u'关掉', u'休息', u'滚开']
		start_cmd = [u'出来', u'启动', u'工作']
		if self.robot_switch:
			for i in stop_cmd:
				if i == msg_data:
					self.robot_switch = False
					self.send_msg_by_uid(u'[Robot]' + u'bye, remember miss me！', msg['to_user_id'])
		else:
			for i in start_cmd:
				if i == msg_data:
					self.robot_switch = True
					self.send_msg_by_uid(u'[Robot]' + u'I am comming！', msg['to_user_id'])

	def handle_msg_all(self, msg):
		# print 'xdc:::::msg:::', self.robot_switch, msg
		# if not self.robot_switch and msg['msg_type_id'] != 1:
		#     return
		# print 'xdc:::::::::', msg
		if msg['msg_type_id'] == 1 and msg['content']['type'] == 0:  # reply to self
			self.auto_switch(msg)
		elif msg['msg_type_id'] == 4 and msg['content']['type'] == 0:  # text message from contact
			self.send_msg_by_uid(self.tuling_auto_reply(msg['user']['id'], msg['content']['data']), msg['user']['id'])
            self.send_img_msg_by_uid('img/1.png', msg['user']['id'])
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
						reply += self.tuling_auto_reply(msg['content']['user']['id'], msg['content']['desc'])
					else:
						reply += u"对不起，只认字，其他杂七杂八的我都不认识，,,Ծ‸Ծ,,"
					self.send_msg_by_uid(reply, msg['user']['id'])
				else:
					reply = self.tuling_auto_reply(msg['content']['user']['id'], msg['content']['desc'])
					self.send_msg_by_uid(reply, msg['user']['id'])

			else:
				reply = self.tuling_auto_reply(msg['content']['user']['id'], msg['content']['desc'])
				self.send_msg_by_uid(reply, msg['user']['id'])
                self.send_img_msg_by_uid('img/1.png', msg['user']['id'])


def main():
	bot = TulingWXBot()
	bot.DEBUG = True
	bot.conf['qr'] = 'png'

	bot.run()


if __name__ == '__main__':
	main()


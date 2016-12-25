#coding:utf-8
import AutoReplyBase
import ConfigParser
import requests
import json

_instance = None
def instance():
	global _instance
	if _instance == None:
		_instance = TulingAutoReply()
	return _instance

# 中文自动回复提供方 图灵
class TulingAutoReply(AutoReplyBase.AutoReplyBase):
	def __init__(self):
		super(TulingAutoReply, self).__init__()
		self.tuling_key = ""
		try:
			cf = ConfigParser.ConfigParser()
			cf.read('conf.ini')
			self.tuling_key = cf.get('main', 'key')
		except Exception:
			pass
		# print 'tuling_key:', self.tuling_key

	def respond(self, uid, msg):
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
			# if result.__class__.__name__ == 'unicode':
			# 	result = result.encode('utf-8')
			print '    ROBOT:', result
			return True, result
		else:
			return False, u"知道啦"


# print instance().respond('123', u'你好')[1]

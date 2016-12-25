#/usr/bin/env python
# coding: utf-8

import httplib
import md5
import urllib
import random
import sys
import json
reload(sys)
sys.setdefaultencoding('utf-8')


appid = '20161015000030242'
secretKey = 'zuWk238Qh2K3iLVNQZjr'

myurl = '/api/trans/vip/translate'
salt = random.randint(32768, 65536)

class BaiduTranslate(object):
	def __init__(self):
		self.httpClient = httplib.HTTPConnection('api.fanyi.baidu.com')

	def translate(self, fromLang, toLang, text):
		sign = appid+text+str(salt)+secretKey
		m1 = md5.new()
		m1.update(sign)
		sign = m1.hexdigest()
		url = myurl+'?appid='+appid+'&q='+urllib.quote(text)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
		result = None
		try:
			self.httpClient.request('GET', url)
			#response是HTTPResponse对象
			response = self.httpClient.getresponse()
			result = response.read()
			result = self.get_result(result)
		except Exception, e:
			print e
		finally:
			if self.httpClient:
				self.httpClient.close()
		return result

	def get_result(self, response):
		res = json.loads(response)
		src = res["trans_result"][0]["src"]
		dst = res["trans_result"][0]["dst"]
		return dst

_instance = None
def instance():
	global _instance
	if _instance == None:
		_instance = BaiduTranslate()
	return _instance

# print instance().translate('en', 'zh', u'hello'.encode('utf-8'))

# a = BaiduTranslate()
# res = a.translate('zh', 'en', u'你在干什么?'.encode('utf-8'))
# print res


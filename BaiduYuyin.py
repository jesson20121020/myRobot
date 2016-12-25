#encoding=utf-8

import wave
import urllib2, pycurl
import base64
import json

API_KEY = "kXX7d1jL7Q7LG1FiVnmBANaK"
SECRET_KEY = "1964498fd86f63a7d276f027b808c850"

class BaiduYuyin(object):
	def __init__(self):
		pass

	def get_token(self):
		auth_url = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=" + API_KEY + "&client_secret=" + SECRET_KEY
		res = urllib2.urlopen(auth_url)
		json_data = res.read()
		return json.loads(json_data)['access_token']

	def voice_to_text(self, voice_file, callback):
		# print 'xdc::::::::voice:::::', voice_file, callback
		fp = wave.open(voice_file, 'rb')
		nf = fp.getnframes()
		f_len = nf * 2
		audio_data = fp.readframes(nf)

		cuid = "xxxxxxxxxx" #my xiaomi phone MAC
		srv_url = 'http://vop.baidu.com/server_api' + '?cuid=' + cuid + '&token=' + self.get_token()
		http_header = [
			'Content-Type: audio/pcm; rate=8000',
			'Content-Length: %d' % f_len
		]
		c = pycurl.Curl()
		c.setopt(pycurl.URL, str(srv_url)) #curl doesn't support unicode
		#c.setopt(c.RETURNTRANSFER, 1)
		c.setopt(c.HTTPHEADER, http_header)   #must be list, not dict
		c.setopt(c.POST, 1)
		c.setopt(c.CONNECTTIMEOUT, 30)
		c.setopt(c.TIMEOUT, 30)
		c.setopt(c.WRITEFUNCTION, callback)
		c.setopt(c.POSTFIELDS, audio_data)
		c.setopt(c.POSTFIELDSIZE, f_len)
		c.perform() #pycurl.perform() has no return val

	def dump_res(self, res):
		import ast
		res = ast.literal_eval(res)
		a =  res.get('result', ['',])[0]
		b =a.decode('utf-8')
		print b


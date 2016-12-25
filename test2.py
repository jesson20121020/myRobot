# coding: utf-8


import requests
from requests.exceptions import ConnectionError, ReadTimeout
import uuid
mac_address=uuid.UUID(int=uuid.getnode()).hex[-12:]


# voice = '49443304000000000018545353450000000e0000034c61766635342e362e31303000ffe328c0000000000000000000496e666f000000070000001a000007e0001b1b1b242424242d2d2d2d3636363640404040494949495252525b5b5b5b646464646d6d6d6d7676767680808080898989929292929b9b9b9ba4a4a4a4adadadadb6b6b6b6c0c0c0c0c9c9c9d2d2d2d2dbdbdbdbe4e4e4e4ededededf6f6f6f6ffffff000000000000000000000000000000ffe318c400093802259008c600c0025a54cb8841f6353ad04dca2e04bebb7f76b1dffca3a70bffff204ffffcbe9fd72ffad2c010ae391f723180aa9a0476f4f6137f8a8135aafd9fffe318c4160998425d98084600ca7bbe9ffea5abefa13ffd7f2886bd1d55800025d92739a13a287f2fe8aff59b262653443120d935a1fead1fd2ffb2fffdd1ffafffffb17ff1eafbffe318c42a0a18c26998084628088a8448830828901408e06061ee45a12ada70aa0e09760ab850b965014825abe7bfeefffffffffffffd158000486e56dce5c4932416780c75cabaffe318c43c0ad8be480028c6283e799efe9fecfa7d9daedf633ebe9edc5bffaf47d9d7d68547f72c6ce020549194618266543e550c9995fbb546726cd0790e15b988a9badeefa7faffe318c44b09e03a5e58088600bfb6f7ffffffeafffea580572db6ddf4074305adbb2db79ffd2a7e5b477fd3eeffffe94fb3ffe8ffedfa95049325b27c15a93b3a81565d8621ec7effe318c45e0b207e44084a4424e43881a166214c573fd9feb7a996f7ff757ffeedbfb3fffd68b3f763132ea500bd8dd6c25938fbd22b3a85089e87e30129574f2c632779a040a581ffe318c46c08100271b800c4000502a2d17842db3e7607e49f4838c83e4dda183456a04286145f5feda9cec57fa28fbd98cffc5bfa55fb99ca9d28cd2a5029a9977b18f883477addffe318c4860ba0626d180bcc0018f280441921755bb0f09f9c62d4af8c10ff96408f4e0524ee77773b5d9d735ffc438e396d5c8c10abfa0a6747bffd7ff22afd63412bd38cb10781ffe318c49211108a6c50d6182499354748339ae4c014ef54b9a52c2830a8e4e447a63747723491c63340aff52d4cb5fcbfbb976df7a685a87ffe925524411a8f57621c6c2ce08262ffe318c48810d9126400de044c8efab33315c4b8010651ddabf57a09f15cc90efebafe0c5daf59d3fd1e8ffffa1bfbfffffdfc99f6458c83fac024cde2e1a58e492d02db75fb2a94ffe318c47f0dc8b27000d630253422243571d63ace506c4bd1d87891c75bdbfa7fffffff986354f75798a380b0020639d40ce666495a8a74215143148eb46d9f6dd5aa8f2affdffeffe318c4820f60ae80789a5e24e9a752f32b291c2b1d407b8994c8d595fbbb9cc182e24cf4ce9b7d5c04b94b5a23bce66ca021b5ac621ea25e3de056d5674cb429d13092bdcdf300ffe318c47f14d2e2be5839c497e82da5b54aa1790673f7c5d622eb13d1efa517b60a6ff161b8833ffbd671322c034182733a877de226733e71a3fabdfd09a74ba127258cc2e3dc2cffe318c4661071ba6400285e7118507266e4b38882a4135f90dcc4d0be99661d8bb6fab03173b753fffffffffdaf272e3392fb26789e0270e719a25d44ba4db04848707ab46b6779ffe318c45f11b98684f0794c70145a3bfe7f9790a5f5244347caad60ac85f902960b1a0608df034cfffffffffff5a2f89e0c087178cd048f24bdc1501459ec52948cf6b2ef4e52d7ffe318c4530e716280c881c64cdd7fcf3febd7b3722aa4b45bdb8a084241208430542132876267d1814a40ef6fcb1ca15bf7be46b3ff91f5bffffb53b6aaf6101b1550143a395677ffe318c4540cf96a700059504cdbfeb1b76ae2d6277ff8dffa697f4a69faaa2834ebb31ea5450d78bcabf6fad34f33def99aa639404a82890094788f47ff7ffd5ffffa7fffc56ae3ffe318c45b0ba95a7998104a4c0e101914055c8d844660d4e4dad146101fd329e51526f15feceecd9a68cfbf5c1153e17dbb2028e59afff6d68dda99d8be9fa2bfe4bbfd1ef4760bffe318c4670a913e581028444c50ba1cdd5ebf1947ffffa9eee8d48686239249319f1bafe5edfed6ffa2857fa7ff77329d0d5e87f77fb6a328b6da36f72a66f97f85013d5fb04a29ffe318c47709786e44002a460567432e20b9f6553dd9f14fd5b95fb97fffd7d5affd3eceffeb3fed927c4404c3c0235c75ab4e63f5fa7bf46efa3d34a56efff60ecf55fe8ff57ffeffe318c48c08f8027258088400ba2ea064f09144ec70500a33872c88344cd6f9226b20d0954759d40d1574929677eb77bbffb58affa9fc45f5bbffd3f5e1da80450b0c90236279acffe318c4a308b0067db8008602a159384e93493088c1a20721d155153a2fe8a88a9ffffb394ca0812826ef58a8b7ff16176767f15169a151416fffff156b4d0ab358ad4c414d4533ffe318c4bb08c05e50500a06002e39392e35555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555ffe318c4d308a0265c5808c4005555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555ffe318c4eb0c207230300992045555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555ffe318c4f50fa92978c849444c5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555'


class SafeSession(requests.Session):
	def request(self, method, url, params=None, data=None, headers=None, cookies=None, files=None, auth=None,
				timeout=None, allow_redirects=True, proxies=None, hooks=None, stream=None, verify=None, cert=None,
				json=None):
		for i in range(3):
			try:
				return super(SafeSession, self).request(method, url, params, data, headers, cookies, files, auth,
														timeout,
														allow_redirects, proxies, hooks, stream, verify, cert, json)
			except Exception as e:
				print e.message, traceback.format_exc()
				continue


session = SafeSession()
session.headers.update({'User-Agent': 'Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5'})

def get_baidu_access_token():
	url = 'https://openapi.baidu.com/oauth/2.0/token?'
	params = {
		'grant_type': 'client_credentials',
		'client_id': 'kXX7d1jL7Q7LG1FiVnmBANaK',
		'client_secret': '1964498fd86f63a7d276f027b808c850',
	}
	r = session.get(url, params=params)
	r.encoding = 'utf-8'
	data = r.json()
	access_token = ''
	if getattr(r, 'status_code', 0) == 200:
		access_token = data.get('access_token', '')

	return access_token


print 'xdc::::', get_baidu_access_token()

# def voice_recognize(voice_data, voice_len):
# 	import base64
# 	voice_data = base64.b64encode(voice_data).decode('utf-8')
# 	voice_len = len(voice_data)
# 	url = 'http://vop.baidu.com/server_api'
# 	headers = {'content-type': 'Content-Type:application/json; charset=UTF-8'}
# 	# params = {
# 	# 	"format":"speex",
# 	# 	"rate":8000,
# 	# 	"channel":1,
# 	# 	"token": "24.f0e71614b9e57a378f5a7d1ddc97bd7d.2592000.1479104801.282335-8749190",
# 	# 	"cuid":"FFAA14EF9693",
# 	# 	"len":voice_len,
# 	# 	"speech":voice_data,
# 	# 	# "url":"https://wx2.qq.com/cgi-bin/mmwebwx-bin/webwxgetvoice?msgid=2313619848041539401&skey=@crypt_754cb97f_d97ccfd6bdb4ba1d9af4b63024c79f72",
# 	# 	# "callback":""

# 	# }

# 	params = {'format':'wav', 'rate':8000, 'channel':1, 'cuid':mac_address, 'token':"24.f27b4516891c498218dbd916bbef5b35.2592000.1479106865.282335-8749190", 'lan':'zh', 'speech':voice_data, 'len':voice_len}

# 	r = session.get(url, params = params)
# 	r.encoding = 'utf-8'
# 	print r
# 	# import json
# 	# data = json.dumps(params, ensure_ascii=False).encode('utf8')
# 	# try:
# 	# 	r = session.post(url, data=data, headers=headers)
# 	# except (ConnectionError, ReadTimeout):
# 	# 	return False
# 	dic = r.json()
# 	print 'xdc:::::::::::::::::::::::::r', dic


# # voice_recognize(voice, 1850)

# headers = {'content-type': 'Content-Type:application/json; charset=UTF-8'}
# url = 'http://japi.juhe.cn/voice_words/getWords'
# f = open('voice_500983863161983171.wav')
# params = {
# 	"key" : "5015c176c0c67474f043027e58f662fa",
# 	"file" : f,
# 	"rate": "8000",
# 	"pname" : "",
# 	"device_id" : "FFAA14EF9693",
# }
# r = session.get(url, params = params)
# print 'r::::::', r
# r.encoding = 'utf-8'
# import json
# # data = json.dumps(params, ensure_ascii=False).encode('utf8')
# try:
# 	r = session.post(url, data=params, headers=headers)
# except (ConnectionError, ReadTimeout):
# 	print 'xxxxxxxxxxxxxxxxx'
# dic = r.json()
# print dic

import base64
import urllib2
import urllib
import json
import wave

def wav_to_text(wav_file):
    try:
        wav_file = open(wav_file, 'rb')
    except IOError:
        print u'文件错误啊，亲'
        return
    wav_file = wave.open(wav_file)
    n_frames = wav_file.getnframes()
    frame_rate = wav_file.getframerate()
    if n_frames != 1 or frame_rate not in (8000, 16000):
        print u'不符合格式'
        return
    audio = wav_file.readframes(n_frames)
    seconds = n_frames/frame_rate+1
    minute = seconds/60 + 1
    for i in range(0, minute):
        sub_audio = audio[i*60*frame_rate:(i+1)*60*frame_rate]
        base_data = base64.b64encode(sub_audio)
        data = {"format": "wav",
                "token": "24.f27b4516891c498218dbd916bbef5b35.2592000.1479106865.282335-8749190",
                "len": len(sub_audio),
                "rate": frame_rate,
                "speech": base_data,
                "cuid": "FF-AA-14-EF-96-93",
                "channel": 1}
        data = json.dumps(data)
        res = urllib2.Request('http://vop.baidu.com/server_api',
                              data,
                              {'content-type': 'application/json'})
        response = urllib2.urlopen(res)
        res_data = json.loads(response.read())
        print res_data['result'][0]

wav_to_text('voice_500983863161983171.wav')

#coding:utf-8
import Utils
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def handle_msg(msg):
	return instance().handle_msg(msg)

_instance = None
def instance():
	global _instance
	if _instance == None:
		_instance = SpecialServiceMgr()
	return _instance

# 特殊服务
class SpecialServiceMgr(object):
	def __init__(self):
		pass

	def handle_msg(self, msg):
		status, result = False, ''
		if isinstance(msg, str):	# 统一转换成uicode编码处理
			msg = msg.decode('utf-8')
		self.msg = msg
		if len(msg) > 3 and (msg[0:2] == '翻译' or msg[0:2] == u'翻译'):
			print msg
			srt = msg[2:].strip().encode('utf-8')
			is_ch = Utils.is_chinese(srt)
			from_lan = ['en', 'zh'][is_ch]
			to_lan = ['zh', 'en'][is_ch]
			import BaiduTranslate
			dst = BaiduTranslate.instance().translate(from_lan, to_lan, srt)
			if dst:
				status = True
				result = u'翻译结果:\n' + dst
		elif len(msg) > 5 and (msg[0:5] == '火车票查询' or msg[0:5] ==
				u'火车票查询'):
			print '火车票查询：'
			data = msg[5:].strip().encode('utf-8')
			data = data.split()
			if len(data) == 3:
				from_station = data[0]
				to_station = data[1]
				date = data[2]
				result = execCmd('python %s %s %s %s' %
						('train_system/tickets.py', from_station, to_station,
					date))
				status = True
			elif len(data) == 4:
				tran_type = data[0]
				from_station = data[1]
				to_station = data[2]
				date = data[3]
				result = execCmd('python %s %s %s %s %s' %('train_system/tickets.py', tran_type,
					from_station, to_station, date))
				status = True
		return status, result

def execCmd(cmd):
	import os
	r = os.popen(cmd)
	text = r.read()
	r.close()
	return text

#print instance().handle_msg(u'火车票查询 上海 西安 2016-12-29')[1]

#encoding:utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import os, commands, glob, re
import datetime

from rpyc import Service
from rpyc.utils.server import ThreadedServer


class remote_call_func(Service):
	
	def exposed_test(self, output):
		print output
		import SpecialServiceMgr
		print 'xdc::::', SpecialServiceMgr.instance().msg
		return SpecialServiceMgr.instance().msg
	
	def exposed_reload(self, module_name):	# 热更新
		import sys
		if module_name in sys.modules:
			module = sys.modules[module_name]
			reload(module)
			return 'reload_module successfully'
		else:
			return '%s is not exist' % module_name


# rpycServer = ThreadedServer(remote_call_func, hostname='localhost', port=11111, auto_register=False)
# rpycServer.start()
#coding:utf-8

def is_chinese(uchar):
	"""判断一个unicode是否是汉字"""
	if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
		return True
	else:
		return False


# def is_number(uchar):
# 	"""判断一个unicode是否是数字"""
# 	if uchar >= u'u0030' and uchar<=u'u0039':
# 		return True
# 	else:
# 		return False


def is_number(s):
	try:
		float(s)
		return True
	except ValueError:
		pass

	try:
		import unicodedata
		unicodedata.numeric(s)
		return True
	except (TypeError, ValueError):
		pass

	return False

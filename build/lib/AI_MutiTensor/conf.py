# -*- coding:utf-8 -*-

"""
config file for muti-tensorflow.
date: 2018/4/2
author: simon

"""

class MutiProcess(object):
	def __init__(self,processlist,arglist=[],filenamelist=[]):

		self.processlist = processlist
		self.arglist = arglist
		self.filenamelist = filenamelist
		if not filenamelist:
			self.filenamelist = [str(i) for i in range(len(processlist))]


# def get_proceseelist():
# 	# add function list in MutiProcess([])
# 	# like: muti = MutiProcess([fun1,fun2],[arg1,arg2],[name1,name2])
# 	#muti = MutiProcess([test1,test2],[27,27],['ss1','ss2'])
# 	return muti
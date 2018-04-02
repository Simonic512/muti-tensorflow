#from LSTM import train
# import functions.

from processtest1 import test1
from processtest2 import test2

class MutiProcess(object):
	
	def __init__(self,processlist,arglist=[],filenamelist=[]):

		self.processlist = processlist
		self.arglist = arglist
		self.filenamelist = filenamelist
		if not filenamelist:
			self.filenamelist = [str(i) for i in range(len(processlist))]


def get_proceseelist():
	# add function list in MutiProcess([])
	# like: muti = MutiProcess([fun1,fun2],[arg1,arg2],[name1,name2])
	muti = MutiProcess([test1,test2],[])
	return muti
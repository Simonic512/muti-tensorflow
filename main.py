# -*- coding:utf-8 -*-

"""
distribution job for GPU and run,

"""


import sys
import multiprocessing
from multiprocessing import Process,current_process
import time
import os

from conf import *

_ , GPUNUM = get_available_gpus()

def get_available_gpus():

	from tensorflow.python.client import device_lib as _device_lib
	local_device_protos = _device_lib.list_local_devices()
	GPUlist = [x.name for x in local_device_protos if x.device_type == 'GPU']
	return GPUlist,len(GPUlist)


def worker3():
	savedStdout = sys.stdout
	file = open('worker3.out','w')
	sys.stdout = file
	job_list = split_worker()[2]
	os.environ["CUDA_VISIBLE_DEVICES"] = '2'
	if job_list:
		for job in job_list:
			job()
	sys.stdout = savedStdout
	file.close()

def get_worker(gpu=0):

	savedStdout = sys.stdout
	job_list,arg_list,name_list = split_worker()
	job_list,arg_list,name_list = job_list[gpu],arg_list[gpu],namelist[gpu]
	os.environ["CUDA_VISIBLE_DEVICES"] = str(gpu)
	if job_list:
		for i,job in enumerate(job_list):
			file = open(name_list[i]+'.out','w')
			sys.stdout = file
			job(arg_list[i])
			file.close()
	print('worker'+str(gpu))
	sys.stdout = savedStdout

def split_worker(gpunums=GPUNUM):
	muti = get_proceseelist()
	job_list = muti.processlist
	arg_list = muti.arglist
	name_list = muti.namelist
	#print(job_list)
	rj,ra,rn = [[] for _ in range(gpunums)],[[] for _ in range(gpunums)],[[] for _ in range(gpunums)]
	for i,job in enumerate(job_list):
		rj[i%gpunums].append(job)
		ra[i%gpunums].append(arg_list[i])
		rn[i%gpunums].append(name_list[i])
	return rj,ra,rn

if __name__ == '__main__':
	# process_list = [Process(target=worker1,args=()),Process(target=worker2,args=()),\
	# Process(target=worker3,args=()),Process(target=worker4,args=())]
	for p in process_list:
	for i in range(GPUNUM):
		process_list.append(Process(target=get_worker,args=(i)))
	for s_p in process_list:
		s_p.start()
	for s_p in process_list:
		s_p.join()

	print('multiprocessing done.')


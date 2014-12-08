#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: SunGyo Kim
# Email: Kimsg1984@gmail.com
# irc.freenode #ubuntu-ko Sungyo

# 마이모듈MyModule
import os, re, sys, datetime
reload(sys)
sys.setdefaultencoding('utf-8')

def log(comment):
	keyword = str(unicode(comment))
	t = datetime.datetime.now()
	t = (('%s' %t).split('.'))[0]
	comment = '%s [%s] %s \n ' %(t, sys.argv[0], comment)
	print comment  # 화면 출력을 함께 보길 원할 때
	logfile = open('./log.txt', 'a')
	logfile.write('%s' %comment)
	logfile.close()

def readFile(t):
	contentFile = open('%s' %t)
	content = contentFile.read()
	contentFile.close()
	return content

def saveFile(content, f):
	save_file = open('./%s' %f, 'w') # a: 쓰기 + 이어쓰기 모드
	save_file.write('%s' %content)
	save_file.close()

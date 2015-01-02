#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: SunGyo Kim
# Email: Kimsg1984@gmail.com
# irc.freenode #ubuntu-ko Sungyo

import re, os, sys, datetime 
import mm # 마이모듈MyModule

reload(sys)
sys.setdefaultencoding('utf-8')
dir_bible = './bible'
file_bible_full ='./bible/bible.txt'
content_bible = str(unicode(mm.readFile(file_bible_full)))

def verbLink(keyword):
	content = sys.argv[1]
	tip = re.findall(r'(^|\s|>)([가-힣]+?)(\d+):(\d+)(~?)', content)
	if len(tip) != 0:
		for t in tip:
			try:
				bible='./bible/%s.txt' %t[1]
				edited_file = open(bible)
				bible_content = edited_file.read()
				if t[4] =='~':
					verb='%s%s:%s~' %(t[1], t[2], t[3])
					n = re.findall(r'%s%s:%s~(\d+)' %(t[1], t[2], t[3]), content)
					try:
						v1 = int(t[3])
						v2 = int(n[0])
						if v2 > v1:
							verb_content=''
							while v2 >= v1:
								verb='%s%s:%d' %(t[1], t[2], v1)
								verb_content_add = re.findall('%s(.+)\n' %(verb), bible_content)
								verb_content='%s(%d)%s '%(verb_content, v1,verb_content_add[0])
								v1 = v1 + 1
							verb='%s%s:%s~%d' %(t[1], t[2], t[3], v2)
							content = content.replace('%s' %(verb), '%s %s' %(verb, verb_content))
					except:
						null = 0

				else:
					try:
						verb='%s%s:%s' %(t[1], t[2], t[3])
						verb_content = re.findall('%s(.+)\n' %(verb), bible_content)
						content = content.replace('%s' %(verb), '%s %s' %(verb, verb_content[0]))
					except:
						null=0
			except:
				null=0
	edited_file.close()
	return content

def search(keyword):
	keyword = str(unicode(keyword))
	# mm.log('search() "%s" ' %keyword)
	content = ''
	l = len(keyword)

	if l > 1 :
		try:
			search = re.findall(r'(^|\n)(.*)%s(.*)' %keyword, content_bible)
			for s in search:
				content = content + '%s%s%s\n\n' %(s[1],keyword,s[2])
		except:
			mm.log('search().fail')
	return content

def openChapter(book, chapter):
	book_content=mm.readFile(os.path.join(dir_bible, book + '.txt'))
	l = len(book)
	keyword = '%s%s' %(book,chapter)
	content = ''
	if l > 1 :
		try:
			search = re.findall(r'%s:(.*)' %keyword, book_content)
			for s in search:
				content =  content +'%s:%s\n\n' %(keyword,s)
		except:
			mm.log('openChapter().fail - book: %(book)s, chapter: %(chapter)s' %vars())
	return content
if __name__ == '__main__':
	null = 0

# test
# 현재 깃 테스트 중이랍니다~~~~~~~^0^
#  이번에는 웹에서 커밋을 해볼게요~~~

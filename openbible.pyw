#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wx, os, re
import booklist

books_number = booklist.books_number
books_fullname = booklist.books_fullname
books_chapters = booklist.books_chapters
title = '열린 성경 - 소프트웨어 저작권이 제대로 열려있는 성경 어플리케이션!'
on_about = """
버전 1.0 - 


열린성경은
오픈소스로 나누는
성경 어플리케이션입니다.

본문 : 개역한글

* 다른 본문도 허락을 받은 후     
  추가 예정입니다. *

e-mail:kimsg1984@gmail.com    """
 
class MyPanel(wx.Panel):

	def __init__(self, parent):
		## HORIZONTAL 옆으로 칸칸, VERTICAL 아래로 칸칸
		wx.Panel.__init__(self, parent)
		self.c = 0
		self.chapters = 0
		self.frame = parent
		self.mainSizer = wx.BoxSizer(wx.HORIZONTAL)		# 메인
		self.leftSizer = wx.BoxSizer(wx.VERTICAL)			# 좌측 패널
		self.controlSizer = wx.BoxSizer(wx.HORIZONTAL)	# 콘트롤 사이저
		self.booklistSizer = wx.BoxSizer(wx.VERTICAL)		# 책 이름이 들어가는 공간
		self.chapterSizer = wx.BoxSizer(wx.VERTICAL) 		# 장 번호가 들어가는 공간
		self.textviewer = wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.TE_READONLY)	# 텍스트 페이지 
		self.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0))			# 폰트설정

		# <책 제목과 장 페이지> ----------------------------------------------------------------------
		self.statebox = wx.StaticBoxSizer(wx.StaticBox(self), wx.HORIZONTAL)
		self.booktitle = wx.StaticText(self, -1, '창세기', style=wx.ALIGN_CENTRE)
        	self.corrent_chapter = wx.StaticText(self, -1, '  1', style=wx.ALIGN_CENTRE)
        	self.last_chapter = wx.StaticText(self, -1,'50', style=wx.ALIGN_CENTRE)
        	self.booktitle.SetFont(wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        	self.last_chapter.SetFont(wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        	self.corrent_chapter.SetFont(wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        	self.statebox.Add(self.booktitle, 0, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 10)
        	self.statebox.Add(self.corrent_chapter, 1, wx.BOTTOM | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND | wx.ALIGN_BOTTOM, 10)
        	self.statebox.Add(self.last_chapter, 1, wx.BOTTOM | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 10)


		# <책 제목과 장 페이지/> ----------------------------------------------------------------------
		
		self.booklistSizer_line = wx.BoxSizer(wx.HORIZONTAL) 	# 한줄 선언
		i=1

		for n in range(1, 67):
			book = books_number[n]
			# print "%(n)d = %(book)s" %vars()
			addButton = wx.Button(self, label=book)
			addButton.label = book
			addButton.SetMinSize((35, 28))
			self.booklistSizer_line.Add(addButton, 0)          	# 단추 넣고
			addButton.Bind(wx.EVT_BUTTON, self.onBook, addButton)	# 바인드

			if i is 4 :
				self.booklistSizer.Add(self.booklistSizer_line, 0)  		# 라인 넣고
				self.booklistSizer_line = wx.BoxSizer(wx.HORIZONTAL)   	# 한줄
				i = 0

			if n is 39 : # 구약 배열 끝난 후 구별선 넣기
				self.booklistSizer.Add(self.booklistSizer_line, 0)  		# 라인 넣고
				self.booklistSizer_line = wx.BoxSizer(wx.HORIZONTAL)   	# 한줄 선언
				static_line = wx.StaticLine(self, -1)				# 구별선 선언
				self.booklistSizer.Add(static_line, 0, wx.EXPAND, 0)
				i = 0

			i += 1

		self.booklistSizer.Add(self.booklistSizer_line, 0)           # 라인 넣고

		## 전체 배열 순서
		self.mainSizer.Add(self.leftSizer, 0)
		self.leftSizer.Add(self.statebox, wx.EXPAND,10)
		self.leftSizer.Add(self.controlSizer, 0)
		self.controlSizer.Add(self.booklistSizer, 0)
		self.controlSizer.Add(self.chapterSizer, 0)
		self.mainSizer.Add(self.textviewer, 1, wx.EXPAND)
		self.SetSizer(self.mainSizer)
	
	def onBook(self, event):
		self.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0))	# 폰트설정
		self.label = event.GetEventObject().label
		self.chapters = books_chapters[self.label]
		self.booktitle.SetLabel(books_fullname[self.label])
		self.last_chapter.SetLabel("%d" %self.chapters)
		
		if self.chapterSizer.GetChildren():
			self.chapterSizer.Hide(0)
		 	self.chapterSizer.Remove(0)

		self.chapterSizerRemoval = wx.BoxSizer(wx.VERTICAL) 	# 지워질꺼니까 리무발~
		self.buttonsLine = wx.BoxSizer(wx.HORIZONTAL)
		i = 1
		
		for r in range(1, self.chapters + 1):
			self.c = r
			number = "%s" %self.c
			chapterButton = wx.Button(self, label=number, name=number)
			chapterButton.number = self.c
			chapterButton.SetMinSize((35, 24))
			self.buttonsLine.Add(chapterButton, 0)
		 	chapterButton.Bind(wx.EVT_BUTTON, self.onChapter, chapterButton)		# 바인드

			if i is 5 :
				self.chapterSizerRemoval.Add(self.buttonsLine, 0)  		
				self.buttonsLine = wx.BoxSizer(wx.HORIZONTAL)
				i = 0
			i += 1
		
		self.chapterSizerRemoval.Add(self.buttonsLine, 0)
		self.chapterSizer.Add(self.chapterSizerRemoval, 0)
		self.frame.fSizer.Layout()
	
	def onChapter(self, event):
		# print event.GetEventObject().number

		# f = open(os.path.join(dir_bible, self.label + '.txt'), 'r')
		# self.textviewer.SetValue(f.read())
		# f.close()

class MyFrame(wx.Frame):

	# def __init__(self):
	def __init__(self, *args, **kwds):
		"""Constructor"""
		# wx.Frame.__init__(self, parent=None, title=title, size=(1024,768))
		# wx.Frame.__init__(self, parent=None, title=title, size=(1024,768))
		kwds["style"] = wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX | wx.MAXIMIZE | wx.MAXIMIZE_BOX | wx.SYSTEM_MENU | wx.RESIZE_BORDER | wx.CLIP_CHILDREN
		wx.Frame.__init__(self, parent=None, title=title, size=(1024, 768), *args, **kwds)
		self.CreateStatusBar() # A Statusbar in the bottom of the window

		# <메뉴> ----------------------------------------------------------------------
		filemenu= wx.Menu()
		menuAbout= filemenu.Append(wx.ID_ABOUT, '오픈성경은..(&A)',' 오픈성경에 대해..')
		menuExit = filemenu.Append(wx.ID_EXIT,'종료(&X)','성경을 종료합니다')
		menuBar = wx.MenuBar()
        	menuBar.Append(filemenu,'파일(&F)') # Adding the "filemenu" to the MenuBar
        	self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.
        	self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        	self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
		# <메뉴/> ----------------------------------------------------------------------
		
		self.fSizer = wx.BoxSizer(wx.HORIZONTAL)
		panel = MyPanel(self)
		self.fSizer.Add(panel, 1, wx.EXPAND)
		self.SetSizer(self.fSizer)
		self.Show()
	
	def OnAbout(self,e):
		dlg = wx.MessageDialog(self, on_about, "About 열린성경", wx.OK)
		dlg.ShowModal() 	
		dlg.Destroy() 	

	def OnExit(self,e):
		self.Close(True)  # Close the frame.
 
if __name__ == "__main__":
	app = wx.App(False)
	frame = MyFrame()
	app.MainLoop()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wx, os, re, sys, inspect
import mm #마이모듈
import booklist, bible

reload(sys)
sys.setdefaultencoding('utf-8')
books_number = booklist.books_number		# 번호별 책 약어
books_fullname = booklist.books_fullname	# 약어별 책 이름
books_chapters = booklist.books_chapters	# 약어별 책 장수
dir = os.getcwd()
title = '오픈바이블 - 열린 저작권으로 나누는 성경 어플리케이션!'
on_about = '''
버전 1.0 

열린성경은
오픈소스로 나누는
성경 어플리케이션입니다.

본문 : 개역한글
툴바디자인:

e-mail:kimsg1984@gmail.com    '''
 
class MyPanel(wx.Panel):

	def __init__(self, parent):
		## HORIZONTAL 옆으로 칸칸, VERTICAL 아래로 칸칸
		wx.Panel.__init__(self, parent)
		self.frame = parent
		self.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0))
		self.main_sizer = wx.BoxSizer(wx.HORIZONTAL)			# 메인
		self.left_sizer = wx.BoxSizer(wx.VERTICAL)			# 좌측 패널 
		self.control_sizer = wx.BoxSizer(wx.HORIZONTAL)	# 콘트롤 사이저
		self.chapter_sizer = wx.BoxSizer(wx.VERTICAL) 		# 장 번호가 들어가는 공간
		self.text_ctrl = wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.TE_READONLY)	# 텍스트 페이지 
		static_line = wx.StaticLine(self, -1)				
		self.booklist_sizer = wx.BoxSizer(wx.VERTICAL)		# 책 이름이 들어가는 공간

		self.book_name = '창'
		self.bible_chapter = '1'
		self.text_ctrl_font_size = 12
		## 프레임과 버튼 생성		
		self.__booklist_sizer_line()
		self.__buttons_line()
		self.__state_box()
		self.__state_box_properties()
		self.__text_ctrl_properties()
		self.__search_box()

		self.__show_and_hide_chapters_button(books_chapters[self.book_name])
		self.text_ctrl.SetValue(bible.openChapter(self.book_name, self.bible_chapter))
		self.__do_layout()

	### Frame Function

	def __booklist_sizer_line(self):
		booklist_sizer_line = wx.BoxSizer(wx.HORIZONTAL) 	# 한줄 선언
		i=1
		for n in range(1, 67):
			book = books_number[n]
			self.button_books = wx.Button(self, label=book)
			self.button_books.book_name_short = book
			self.button_books.SetMinSize((35, 28))
			booklist_sizer_line.Add(self.button_books, 0)
			self.button_books.Bind(wx.EVT_BUTTON, self.onBook, self.button_books)

			if i is 4 :
				self.booklist_sizer.Add(booklist_sizer_line, 0)  		
				booklist_sizer_line = wx.BoxSizer(wx.HORIZONTAL)   	
				i = 0

			if n is 39 : # 구약 배열 끝난 후 구별선 넣기
				self.booklist_sizer.Add(booklist_sizer_line, 0)  		
				booklist_sizer_line = wx.BoxSizer(wx.HORIZONTAL)   	
				static_line = wx.StaticLine(self, -1)				
				self.booklist_sizer.Add(static_line, 0, wx.EXPAND, 0)
				i = 0

			i += 1
		self.booklist_sizer.Add(booklist_sizer_line, 0)

	def __buttons_line(self):
		self.buttons_line_group = []
		buttons_line = wx.BoxSizer(wx.HORIZONTAL)

		i = 1
		for number in range(1, 151):
			number = '%s' %number
			self.button_chapter = wx.Button(self, label=number, name=number)
			self.button_chapter.number = number
			self.button_chapter.SetMinSize((35, 22))
			buttons_line.Add(self.button_chapter, 0)
		 	self.button_chapter.Bind(wx.EVT_BUTTON, self.onChapter, self.button_chapter)
			if i is 5 :
				self.buttons_line_group.append(buttons_line)
				buttons_line = wx.BoxSizer(wx.HORIZONTAL)
				i = 0
			i += 1
		if i is not 1:
			self.buttons_line_group.append(buttons_line)
		for b in self.buttons_line_group:
			self.chapter_sizer.Add(b, 0)

	def __state_box(self):
        	
        	def addBoxSizer(static_text, w, h, align): # 창 크기와 여백 설정을 위한 함수
	        	box_sizer = wx.BoxSizer(wx.VERTICAL)
	        	box_sizer.AddSpacer((w,h))
	        	box_sizer.Add(static_text, 0, align)
        		self.state_box.Add(box_sizer, 0, 10)

		self.state_box = wx.StaticBoxSizer(wx.StaticBox(self), wx.HORIZONTAL)
		self.book_title = wx.StaticText(self, -1, books_fullname[self.book_name])
        	self.corrent_chapter = wx.StaticText(self, -1, self.bible_chapter)
        	self.last_chapter = wx.StaticText(self, -1, '%s' %books_chapters[self.book_name])

        	addBoxSizer(self.corrent_chapter, 25, 7, wx.ALIGN_RIGHT)
        	self.state_box.AddSpacer((20, 0))
        	addBoxSizer(self.last_chapter, 30, 10, wx.ALIGN_LEFT)
        	addBoxSizer(self.book_title, 150, 5, wx.ALIGN_LEFT)

	def __state_box_properties(self):
		self.state_box.SetMinSize((315, -1))
        	self.book_title.SetFont(wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ''))
        	self.corrent_chapter.SetFont(wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ''))
        	self.last_chapter.SetFont(wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ''))
        	
	def __text_ctrl_properties(self):
		self.text_ctrl.SetFont(wx.Font(self.text_ctrl_font_size, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ''))

	def __search_box(self):
		search_box_sizer = wx.BoxSizer(wx.HORIZONTAL)
		static_line = wx.StaticLine(self, -1)
		self.search_box = wx.TextCtrl(self, -1, "", (-1,-1), (80, -1))
		self.search_button = wx.Button(self, label='검색', name='검색')
		self.search_button.SetMinSize((50, 25))
		self.search_button.Bind(wx.EVT_BUTTON, self.onSearch)
		self.search_box.Bind(wx.EVT_KEY_UP, self.OnKeyUp)
		search_box_sizer.Add(self.search_box, 0,0,0)
		search_box_sizer.Add(self.search_button, 0)
		self.booklist_sizer.Add(static_line, 0, wx.EXPAND, 0)
		self.booklist_sizer.Add(search_box_sizer, 0,0,0)

	def __do_layout(self):
		self.main_sizer.Add(self.left_sizer, 0)
		self.left_sizer.Add(self.state_box, wx.EXPAND,0)
		self.left_sizer.Add(self.control_sizer, 0)
		self.control_sizer.Add(self.booklist_sizer, 0)
		self.control_sizer.Add(self.chapter_sizer, 0)
		self.main_sizer.Add(self.text_ctrl, 1, wx.EXPAND)
		self.SetSizer(self.main_sizer)
	
	def __show_and_hide_chapters_button(self, chapters):
		button_number = 1
		for line_number in range(1, 31):
			if button_number <= chapters:
				if button_number <= 70: # 70장 이상은 시편뿐. 라인만 켠다.
					for column_number in range(1, 6):
						if column_number is 1:
							self.chapter_sizer.Show(line_number-1) # 첫번째 단추를 켤 때 라인도 함께 켜기
						button_number += 1
						if button_number <= chapters + 1:
							self.buttons_line_group[line_number-1].Show(column_number-1)
						else:
							self.buttons_line_group[line_number-1].Hide(column_number-1)
				else:
					self.chapter_sizer.Show(line_number-1)
			else:
				self.chapter_sizer.Hide(line_number-1)
				
	### Moving Function
		
	def OnKeyUp(self, event):
		code = event.GetKeyCode()
		if code == wx.WXK_RETURN:
			self.onSearch('null')
		event.Skip()
	
	def onSearch(self, event):
		keyword = '%s'  %self.search_box.GetValue()
		if len(keyword) >= 1 and keyword is not ' ':
			content = bible.search(keyword)
			self.text_ctrl.SetValue(content)
			textviewer_split = self.text_ctrl.GetValue().split(keyword)
			keyword_len = len(keyword)
			position = []
			dist = 0

			for t in textviewer_split:
				dist += len(t)
				position.append(dist)
				dist += keyword_len

			for p in position:
				self.text_ctrl.SetStyle(p, p+keyword_len, wx.TextAttr('black', 'yellow'))

	def onBook(self, event):
		try:
			self.book_name = event.GetEventObject().book_name_short  # Ex) 창, 출, 레...
		except: 
			self.book_name = self.book_name

		chapters = books_chapters[self.book_name]
		self.book_title.SetLabel(books_fullname[self.book_name])
		self.last_chapter.SetLabel('%d' %chapters)
		self.__show_and_hide_chapters_button(chapters)
		self.onChapter('null')
		self.frame.f_sizer.Layout()

			
	def onChapter(self, event):
		try:	
			self.bible_chapter = event.GetEventObject().number
		except:
			self.bible_chapter = self.bible_chapter

		self.corrent_chapter.SetLabel('%s' %self.bible_chapter)
		self.text_ctrl.SetValue(bible.openChapter(self.book_name, self.bible_chapter))
		self.SetSizer(self.main_sizer)

class MyFrame(wx.Frame):

	def __init__(self, *args, **kwds):
		kwds['style'] = wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX | wx.MAXIMIZE | wx.SYSTEM_MENU | wx.RESIZE_BORDER | wx.CLIP_CHILDREN
		# kwds['style'] = wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX | wx.MAXIMIZE | wx.MAXIMIZE_BOX | wx.SYSTEM_MENU | wx.RESIZE_BORDER | wx.CLIP_CHILDREN
		wx.Frame.__init__(self, parent=None, title=title, size=(1024, 768), *args, **kwds)
		self.status_bar = self.CreateStatusBar() # A Statusbar in the bottom of the window

		self.__menubar()	
		self.__toolbar()	
		panel = MyPanel(self)
		self.f_sizer = wx.BoxSizer(wx.VERTICAL)
		self.f_sizer.Add(self.toolbar, 0, wx.EXPAND)
		self.f_sizer.Add(panel, 1, wx.EXPAND)
		self.SetSizer(self.f_sizer)
		self.Show()
	
	def __menubar(self):
		filemenu= wx.Menu()
		menu_about= filemenu.Append(wx.ID_ABOUT, '오픈바이블은..(&A)',' 오픈바이블에 대해..')
		menu_exit = filemenu.Append(wx.ID_EXIT,'종료(&X)','오픈바이블을 종료합니다')
		menubar = wx.MenuBar()
        	menubar.Append(filemenu,'파일(&F)') 	# Adding the 'filemenu' to the menubar
        	self.SetMenuBar(menubar)  			# Adding the menubar to the Frame content.
        	self.Bind(wx.EVT_MENU, self.manubar_OnExit, menu_exit)
        	self.Bind(wx.EVT_MENU, self.manubar_OnAbout, menu_about)

	def manubar_OnAbout(self, event):
		dlg = wx.MessageDialog(self, on_about, 'About 오픈바이블', wx.OK)
		dlg.ShowModal() 	
		dlg.Destroy() 	

	def manubar_OnExit(self, event):
		self.Close(True)

	def __toolbar(self):
		self.toolbar = wx.ToolBar(self)
		self.toolbar.AddSeparator()
		toolbar_menu_on_off = self.toolbar.AddLabelTool(wx.ID_ANY, 'test', wx.Bitmap(os.path.join(dir, './icon/boxx_S.png')), shortHelp='메뉴 펴기/접기', longHelp='좌측의 성경메뉴 화면을 펴고 접습니다.')
		self.toolbar.AddSeparator()
		toolbar_font_bigger = self.toolbar.AddLabelTool(wx.ID_ANY, 'test', wx.Bitmap(os.path.join(dir, './icon/A+_S.png')), shortHelp='글씨 크게', longHelp='성경 본문의 글씨를 키웁니다.')
		toolbar_font_smaller = self.toolbar.AddLabelTool(wx.ID_ANY, 'test', wx.Bitmap(os.path.join(dir, './icon/A-_SS.png')), shortHelp='글씨 작게', longHelp='성경 본문의 글씨를 줄입니다.')
		self.toolbar.AddSeparator()
		toolbar_chapter_prior = self.toolbar.AddLabelTool(wx.ID_ANY, 'test', wx.Bitmap(os.path.join(dir, './icon/play_L_S.png')), shortHelp='이전 장', longHelp='이전 장으로 돌아갑니다.')
		toolbar_chapter_next = self.toolbar.AddLabelTool(wx.ID_ANY, 'test', wx.Bitmap(os.path.join(dir, './icon/play_R_S.png')), shortHelp='다음 장', longHelp='다음 장으로 넘어갑니다.')
		self.toolbar.Realize()

		self.Bind(wx.EVT_TOOL, self.toolbar_MenuOnOff, toolbar_menu_on_off)
		self.Bind(wx.EVT_TOOL, self.toolbar_Font(MyPanel.text_ctrl_font_size + 1), toolbar_font_bigger)
		self.Bind(wx.EVT_TOOL, self.toolbar_Font(MyPanel.text_ctrl_font_size - 1), toolbar_font_smaller)
		self.Bind(wx.EVT_TOOL, self.test, toolbar_chapter_prior)
		self.Bind(wx.EVT_TOOL, self.test, toolbar_chapter_next)
	
	def toolbar_MenuOnOff(self, event):
		print 'test'
		print event
	
	def toolbar_Font(self, font_size):
		print font_size
 
if __name__ == '__main__':
	app = wx.App(False)
	frame = MyFrame()
	app.MainLoop()

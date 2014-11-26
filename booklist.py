#!/usr/bin/env python
# -*- coding: utf-8 -*-

books_number={1:'창', 2:'출', 3:'레', 4:'민', 5:'신', 6:'수', 7:'삿', 8:'룻', 9:'삼상', 10:'삼하', 11:'왕상', 12:'왕하', 13:'대상', 14:'대하', 15:'스', 16:'느', 17:'에', 18:'욥', 19:'시', 20:'잠', 21:'전', 22:'아', 23:'사', 24:'렘', 25:'애', 26:'겔', 27:'단', 28:'호', 29:'욜', 30:'암', 31:'옵', 32:'욘', 33:'미', 34:'나', 35:'합', 36:'습', 37:'학', 38:'슥', 39:'말', 40:'마', 41:'막', 42:'눅', 43:'요', 44:'행', 45:'롬', 46:'고전', 47:'고후', 48:'갈', 49:'엡', 50:'빌', 51:'골', 52:'살전', 53:'살후', 54:'딤전', 55:'딤후', 56:'딛', 57:'몬', 58:'히', 59:'약', 60:'벧전', 61:'벧후', 62:'요일', 63:'요이', 64:'요삼', 65:'유', 66:'계', }

books_fullname = {'창':'창세기', '출':'출애굽기', '레':'레위기', '민':'민수기', '신':'신명기', '수':'여호수아', '삿':'사사기', '룻':'룻기', '삼상':'사무엘상', '삼하':'사무엘하', '왕상':'열왕기상', '왕하':'열왕기하', '대상':'역대상', '대하':'역대하','스':'에스라', '느':'느헤미야', '에':'에스라', '욥':'욥기', '시':'시편', '잠':'잠언', '전':'전도서', '아':'아가서', '사':'이사야', '렘':'예레미야', '애':'예레미야애가', '겔':'에스겔', '단':'다니엘', '호':'호세아', '욜':'요엘', '암':'아모스', '옵':'오바댜', '욘':'요나', '미':'미가', '나':'나훔', '합':'하박국', '습':'스바냐', '학':'학개', '슥':'스가랴', '말':'말라기', '마':'마태복음', '막':'마가복음', '눅':'누가복음', '요':'요한복음', '행':'사도행전', '롬':'로마서', '고전':'고린도전서', '고후':'고린도후서', '갈':'갈라디아서', '엡':'에베소서', '빌':'빌립보서', '골':'골로새서', '살전':'데살로니가전서', '살후':'데살로니가후서', '딤전':'디모데전서', '딤후':'디모데후서', '딛':'디도서', '몬':'빌레몬서', '히':'히브리서', '약':'야고보서', '벧전':'베드로전서', '벧후':'베드로후서', '요일':'요한일서', '요이':'요한이서', '요삼':'요한삼서', '유':'유다서', '계':'요한계시록'}

books_chapters = {'창':50, '출':40, '레':27, '민':36, '신':34, '수':24, '삿':21, '룻':4, '삼상':31, '삼하':24, '왕상':22, '왕하':25, '대상':29, '대하':36,'스':10, '느':13, '에':10, '욥':42, '시':150, '잠':31, '전':12, '아':8, '사':66, '렘':52, '애':5, '겔':48, '단':12, '호':14, '욜':3, '암':9, '옵':1, '욘':4, '미':7, '나':3, '합':3, '습':3, '학':2, '슥':14, '말':4, '마':28, '막':16, '눅':24, '요':21, '행':28, '롬':16, '고전':16, '고후':13, '갈':6, '엡':6, '빌':4, '골':4, '살전':5, '살후':3, '딤전':6, '딤후':4, '딛':3, '몬':1, '히':13, '약':5, '벧전':5, '벧후':3, '요일':5, '요이':1, '요삼':1, '유':1, '계':22}

if __name__ == "__main__":
	for i in range(1, 66):
		book = books_number[i]
		print book

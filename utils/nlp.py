#!/usr/bin/env python3
print("Load...")
import re,os
import pymorphy2
morph = pymorphy2.MorphAnalyzer()

import pymystem3
mstm = pymystem3.Mystem()
mstm.start()

NAMES=['Егор', 'Серик', 'Марианна', 'Роза', 'Валера', 'Валерий', 'Владислав', 'Снежана', 'Наташа', 'Аля', 'Владимир', 'Катерина', 'Алена', 'Елена', 'Стас',
'Алеся', 'Татьяна', 'Рустам', 'Лера', 'Даша', 'Яночка', 'Инга', 'Адам', 'Глеб', 'Венера', 'Евгения', 'Павло', 'Никита', 'Антонина', 'Надя', 'София', 'Валентин',
'Айнур', 'Ярик', 'Ильдар', 'Кирилл', 'Леха', 'Ксения', 'Матвей', 'Жека', 'Алик', 'Олька', 'Альберт', 'Лёха', 'Владлена', 'Иришка', 'Артем', 'Мария', 'Варвара',
'Коля', 'Альбина', 'Дмитрий', 'Катюша', 'Саша', 'Мирослава', 'Люба', 'Снежанна', 'Алиса', 'Евгений', 'Зинаида', 'Настя', 'Владик', 'Сашка', 'Анастасия',
'Борис', 'Костя', 'Марат', 'Марк', 'Ренат', 'Юрий', 'Маргарита', 'Ната', 'Илона', 'Дарига', 'Жанар', 'Зарина', 'Оксана', 'Маринка', 'Лёша', 'Викуся',
'Рома', 'Данил', 'Лидия', 'Мурад', 'Алишер', 'Танюшка', 'Камилла', 'Димон', 'Айбек', 'Тамара', 'Георгий', 'Олег', 'Дарья', 'Роман', 'Яна',
'Ева', 'Алёна', 'Люда', 'Леонид', 'Валентина', 'Иван', 'Катя', 'Софа', 'Аскар', 'Василий', 'Вадим', 'Федор', 'Гена', 'Виталий', 'Эвелина', 'Григорий',
'Зоя', 'Лина', 'Нина', 'Ибрагим', 'Иннокентий', 'Света', 'Дина', 'Светлана', 'Марина', 'Алекс', 'Anton', 'Ира', 'Нурлан', 'Сашуля', 'Юра', 'Владимер',
'Амина', 'Лена', 'Володя', 'Регина', 'Назар', 'Сабина', 'Денис', 'Артём', 'Слава', 'Юля', 'Олечка', 'Лиля', 'Филипп', 'Лейла', 'Серафима', 'Нурик',
'Дана', 'Ринат', 'Римма', 'Натали', 'Анжела', 'Виолетта', 'Тимур', 'Михаил', 'Эльмира', 'Гульнара', 'Эльвира', 'Женя', 'Макс', 'Магомед', 'Клавдия',
'Кира', 'Леночка', 'Марьяна', 'Марта', 'Фатима', 'Вася', 'Кирил', 'Ольга', 'Даниил', 'Ильнур', 'Динара', 'Алла', 'Полина', 'Дима', 'Саня', 'Леся',
'Вера', 'Тимофей', 'Вика', 'Раиса', 'Людмила', 'Шамиль', 'Анатолий', 'Лариса', 'Диана', 'Ксюша', 'Настюша', 'Рита', 'Маржан', 'Василиса', 'Жора',
'Майя', 'Алевтина', 'Αртем', 'Соня', 'Николай', 'Лиза', 'Дамир', 'Паша', 'Таисия', 'Карина', 'Наталия', 'Юляшка', 'Андрюха', 'Пётр', 'Анюта',
'Валя', 'Милана', 'Катюшка', 'Александр', 'Арсений', 'Танюша', 'Алинка', 'Виктор', 'Арсен', 'Sergey', 'Агата', 'Aleksandra', 'Вячеслав',
'Гуля', 'Надежда', 'Толик', 'Андрей', 'Лев', 'Арина', 'Серёга', 'Василь', 'Вероника', 'Артур', 'Ирина', 'Настюшка', 'Валерия', 'Фёдор',
'Мадина', 'Степан', 'Аня', 'Вован', 'Мила', 'Анна', 'Жанна', 'Руслан', 'Эдуард', 'Леша', 'Захар', 'Станислав', 'Ульяна', 'Богдан',
'Максим', 'Маша', 'Ваня', 'Петя', 'Таня', 'Серёжа', 'Влада', 'Юленька', 'Миша', 'Рамиль', 'Дарина', 'Игорь', 'Ангелина', 'Кристина',
'Давид', 'Юлия', 'Витя', 'Алина', 'Азамат', 'Аслан', 'Виталя', 'Мишка', 'Артемий', 'Петр', 'Колян', 'Алексей', 'Анфиса', 'Виктория',
'Инна', 'Семён', 'Элеонора', 'Наталья', 'Эдик', 'Гриша', 'Сергей', 'Ярослав', 'Мухаммад', 'Вова', 'Константин', 'Пашка', 'Ден', 'Антон',
'Азат', 'Ника', 'Равиль', 'Алия', 'Елизавета', 'Серега', 'Юличка', 'Лилия', 'Даня', 'Сережа', 'Олеся', 'Радик', 'Влад', 'Анечка', 'Толя',
'Некит','Димка', 'Юль', 'Гоша',"Костян", "Люся", "Люси", "Курису",
"Родион","Ирочка","Натаха","Наталя","Серёг","Веня","Илюха","Рената","Ариночка",
'Софья', 'Рашид', 'Надюша', 'Анита', 'Илья', 'Оля', 'Галина', 'Галя', 'Саида', 'Тарас', 'Анжелика', 'Федя', 'Павел', 'Александра']

def isItName(s):
	'''
	Return true if s is human Name
	'''
	if(s=="Любовь"):return True
	if(len(s)<2):
		return False
	return s[0].upper()+s[1:].lower() in NAMES

badword_pattern=re.compile("[а-яА-Я]+\*+[а-яА-Я]+")
badword_pattern2=re.compile("[а-яА-Я]+\*+")
badword_pattern3=re.compile("\*+[а-яА-Я]+")

def deleteBadWordsCens(text):
	'''
	Replace "феерический д***о**" to "феерический дqqqоqq"
	Need for Mystem
	'''
	badwords=badword_pattern.findall(text)
	for bw in badwords:
		text=text.replace(bw,bw.replace("*","q"))
	badwords2=badword_pattern2.findall(text)
	for bw in badwords2:
		text=text.replace(bw,bw.replace("*","q"))
	badwords3=badword_pattern3.findall(text)
	for bw in badwords3:
		text=text.replace(bw,bw.replace("*","q"))
	return text

def lemmatization(text):
	'''
	Set all words to start form, save info. Good function, uses deep_lemmatize
	Main function for this module
	return lemmatizated string and array with information from Mystem and pymorphy2
	'''
	if(text.replace(" ","")==""):return ('', [{'text': ' '}])
	text=text.replace("&gt;",">").replace("&lt;","<").replace("&amp;","&")
	text = re.sub('((www\\.[^\\s]+)|(https?://[^\\s]+))','URL', text)
	text = re.sub('@[^\\s]+','USER', text)
	text = re.sub('\[id[0-9]+\|[\s\S]+\]','USER', text)
	text = re.sub('\[id[0-9]+\:[a-zA-Z\-\_0-9]+\|[\s\S]+\]','USER', text)
	badwords=badword_pattern.findall(text)
	for bw in badwords:
		text=text.replace(bw,bw.replace("*","q"))
	badwords2=badword_pattern2.findall(text)
	for bw in badwords2:
		text=text.replace(bw,bw.replace("*","q"))
	badwords3=badword_pattern3.findall(text)
	for bw in badwords3:
		text=text.replace(bw,bw.replace("*","q"))
	text = re.sub('и\/или','или', text)
	text = re.sub('2к[0-9][0-9]','YEAR', text)
	text = re.sub('20[0-9][0-9]','YEAR', text)
	text = re.sub('19[0-9][0-9]','YEAR', text)
	text = re.sub('[12]?[0-9][0-9]\.[12]?[0-9][0-9]\.[12]?[0-9][0-9]\.[12]?[0-9][0-9]','IPVFOUR', text)
	text = re.sub('[0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F]','MAC', text)
	text = re.sub('[0-9a-fA-F][0-9a-fA-F]\-[0-9a-fA-F][0-9a-fA-F]\-[0-9a-fA-F][0-9a-fA-F]\-[0-9a-fA-F][0-9a-fA-F]\-[0-9a-fA-F][0-9a-fA-F]\-[0-9a-fA-F][0-9a-fA-F]','MAC', text)
	text = re.sub('[0-9a-fA-F][0-9a-fA-F]\.[0-9a-fA-F][0-9a-fA-F]\.[0-9a-fA-F][0-9a-fA-F]\.[0-9a-fA-F][0-9a-fA-F]\.[0-9a-fA-F][0-9a-fA-F]\.[0-9a-fA-F][0-9a-fA-F]','MAC', text)
	text = re.sub('[0-9][0-9][0-9][0-9]\ [0-9][0-9][0-9][0-9]\ [0-9][0-9][0-9][0-9]\ [0-9][0-9][0-9][0-9]','CARD', text)
	text = re.sub('[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]','CARD', text)
	text = re.sub('[0-9]+к','NUM', text)
	text = re.sub('[0-9]+','NUM', text)
	text = re.sub('NUM( NUM)+','NUM', text)
	text = re.sub('NUM[\,\.]NUM','NUMREAL', text)
	text = re.sub('\$\ ?NUM','COIN', text)
	text = re.sub('NUM\ ?\$','COIN', text)
	text=text.replace("\""," ").replace("'s"," is").replace("'"," ").replace("«"," ").replace("»"," ").replace("{"," ").replace("}"," ")
	text=text.replace("\\"," ").replace("/"," ")
	text=text.replace("…","...").replace("“"," ").replace("”"," ")
	text=text.replace(" - "," — ").replace(")))",")").replace("(((","(").replace("\\"," ").replace("/"," ")
	text=text.replace("#"," ").replace("--—"," ").replace(" -- "," — ").replace("- "," ")
	text = re.sub('\++','+', text)
	text = re.sub('\)\)+','))', text)
	text = re.sub('\(\(+','((', text)
	text = re.sub('[тТT]\.\ ?[дД]\.','т_д', text)
	text = re.sub('[тТT]\.\ ?[Пп]\.','т_п', text)
	text = re.sub('[cCсС][cCсС][cCсС][рРpP]','USSR', text)
	text = re.sub(' +',' ', text)
	tmp=''
	for i in range(len(text)-2):
		if(text[i]==text[i+1] and text[i]==text[i+2]):tmp+=text[i]
	for i in tmp:
		if(i=='.'):text = re.sub(("\\"+i)*3+"+",i+i+i, text)
		else:
			while(i*3 in text):text = text.replace(i*3,i*2)
	arr=deep_lemmatize(text)
	outp=[]
	for i in arr:
		if(not 'analysis' in i):continue
		if isItName(i['pymorphy_nform']): outp.append('USER')
		elif i['pymorphy_nform']=='ия': outp.append('ИИ')
		elif i['pymorphy_nform']=='курис': outp.append('Курису')
		elif i['pymorphy_nform']=='макис': outp.append('Макисэ')
		else: outp.append(i['pymorphy_nform'])
	tmp=" ".join(outp).replace("..."," ").replace(","," ").replace("?",". ").replace("!",". ").replace(":"," ").replace(" — "," ")
	tmp=re.sub(' +',' ', tmp)
	if(len(tmp)==0):return "",arr
	if(tmp[-1]==" " or tmp[-1]=="\n"):return tmp[:-1],arr
	return tmp,arr

def getBestParse(mstd):
	'''
	Find best pymorphy parse result for Mystem analise dict
	'''
	values=morph.parse(mstd['text'])
	if(len(values)<1):
		return values[0]
	mstmTags=None
	try:
		mstmTags=mstd['analysis'][0]['gr']
	except:
		mstmTags='APRO|ANUM|NUM|S=(вин,мн,ед,муж,жен,неод|им,мн,ед,муж,жен)'
	mstmTags=mstmTags.replace("ADV=","ADVB").replace("ADV,","ADVB").replace("A=","ADJF").replace("A,","ADJF")
	mstmTags=mstmTags.replace("ADVPRO","ADVB").replace("ANUM","ADJF").replace("APRO","ADJF")
	mstmTags=mstmTags.replace("ADVPRO","ADVB").replace("ANUM","ADJF").replace("APRO","ADJF")
	mstmTags=mstmTags.replace("NUM","NUMR").replace("PART","PRCL").replace("PR=","PREP").replace("PR,","PREP")
	mstmTags=mstmTags.replace("S=","NOUN").replace("S,","NOUN").replace("SPRO","NPRO")
	mstmTags=mstmTags.replace("S=","NOUN").replace("S,","NOUN").replace("SPRO","NPRO")
	mstmTags=mstmTags.replace("V=","VERB").replace("V,","VERB")
	if("инф" in mstmTags and "VERB" in mstmTags):mstmTags.replace("VERB","INFN")
	tmp=[]
	for v in values:
		part=list(v.tag.grammemes)
		part.sort()
		part=part[0]
		tt=list(v.tag.grammemes_cyr)
		tt.sort()
		try:
			tt=[part]+tt[1:]
		except:
			tt=[part]
		count=0
		for l in tt:
			count+=int(l in mstmTags)
		tmp.append(count)
	return values[tmp.index(max(tmp))]

def deep_lemmatize(text):
	'''
	Make quality lemmatizatien, e.g. "Я на льду" -> "Я на лёд", so slow
	'''
	arr=None
	try:
		arr=mstm.analyze(text)
	except BrokenPipeError:
		print("Warning: restart Mystem backend")
		mstm.close()
		mstm.start()
		return deep_lemmatize(text)
	if(arr[-1]['text']=='\n'):arr=arr[:-1]
	for l in arr:
		if('analysis' in l.keys()):
			tmp=getBestParse(l)
			l['pymorphy_tags']=tmp.tag
			l['pymorphy_nform']=tmp.normal_form
	return arr

def postprocessing_text(text):
	'''
	Return some preprocessed tokens as word
	'''
	if("всё" in text):print("fixme: всё и все не всегда понимаются правильно")
	text=text.replace("USSR","СССР").replace("всё","все").replace("т_д","т.д.").replace("т_п","т.п.")
	for n in NAMES:
		if(n[-1] in "ая"):
			text=text.replace(n[:-1].lower(),n[:-1])
		else:
			text=text.replace(n.lower(),n)
	return text

def OpenTag2str(tags,delimeter="_"):
	'''
	Convert OpenCorpora tags to russian string
	'''
	return tags.cyr_repr.replace(",",delimeter).replace(" ",delimeter)

def get_wordforms(arr):
	'''
	Get array from lemmatization(text) as argument
	return string of word forms, commas and etc...
	'''
	res=[]
	for i in arr:
		if(i['text'] in ['NUM','NUMREAL','USER','COIN','URL','YEAR','IPVFOUR','MAC','CARD']):
			res.append(i['text'])
		elif("," in i['text']):res.append('ЗПТ')
		elif("—" in i['text']):res.append('ТИРЕ')
		elif("." in i['text']):res.append('ТЧК')
		elif(":" in i['text']):res.append('ДВТЧК')
		elif("?" in i['text']):res.append('ВПР')
		elif("!" in i['text']):res.append('ВСКЛ')
		elif("..." in i['text']):res.append('МНТЧК')
		elif("…" in i['text']):res.append('МНТЧК')
		elif('pymorphy_tags' in i):
			tags=i['pymorphy_tags']
			if(tags.POS in ['PREP','CONJ','PRCL','INTJ']):
				res.append(i['text'])
			else:
				res.append(OpenTag2str(tags,""))
		else:res.append(i['text'])
	res.append('END')
	tmp=re.sub(' +',' '," ".join(res))
	if(tmp[-1]==" " or tmp[-1]=="\n"):return tmp[:-1]
	return tmp

def buildTextByForms(lems,forms):
	'''
	Build text. Example:
	lems='мама кататься по лёд и упасть следом упасть весь сестра брат'
	forms='СУЩоджредим ГЛнесовнеперехжредпрошизъяв по СУЩнеодмредпр2 и ГЛсовнеперехжредпрошизъяв ТЧК Н ГЛсовнеперехмнпрошизъяв ПРИЛмест-псредим ДВТЧК СУЩоджредим ЗПТ СУЩодмредим ТЧК END'
	return "Мама каталась по льду и упала. Следом упали все: сестра, брат..."
	'''
	if(type(lems)==str):lems=lems.split(" ")
	if(type(forms)==str):forms=forms.split(" ")
	res=[]
	j=0
	for i in range(len(forms)):
		f=forms[i]
		if(f=="END"):break
		elif(f=="ЗПТ"):
			res.append(",")
			j+=1
		elif(f=="ТИРЕ"):
			res.append("—")
			j+=1
		elif(f=="ТЧК"):
			res.append(".")
			j+=1
		elif(f=="ДВТЧК"):
			res.append(":")
			j+=1
		elif(f=="ВПР"):
			res.append("?")
			j+=1
		elif(f=="ВСКЛ"):
			res.append("!")
			j+=1
		elif(f=="МНТЧК"):
			res.append("...")
			j+=1
		else:
			w=lems[i-j]
			if(f==w):res.append(w)
			else:
				ww=morph.parse(w)[0].lexeme
				isOK=False
				for l in ww:
					if(OpenTag2str(l.tag,"")==f):
						res.append(l.word)
						if(i==0 or forms[i-1] in ["ТЧК","ВПР","ВСКЛ","МНТЧК"]):res[-1]=res[-1][0].upper()+res[-1][1:]
						isOK=True
						break
				if(not isOK):res.append("["+w+"->"+f+"]")
	tmp=" ".join(res)
	tmp=tmp.replace(" .",".").replace(" :",":").replace(" !","!").replace(" ?","?").replace(" ...","...").replace(" ,",",")
	tmp=re.sub(' +',' ',tmp)
	if(tmp[-1]==" " or tmp[-1]=="\n"):return tmp[:-1]
	return tmp

print("Loaded")

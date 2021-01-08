#!/usr/bin/env python3
print("Loading...")
import os,sys,pickle
import gensim
import numpy as np

modelsPath=os.path.dirname(__file__)+"/w2v_models/"
print("Path for gensim models set up as",modelsPath)

staticmodels=[]
trainablemodels=[]

def loadModel(fname,trainable=True):
	'''
	Load word2vec gensim model by fname. If it is pickle object it can be trainable
	'''
	global staticmodels,trainablemodels
	try:
		if(fname[-4:].lower()==".bin"):#Static saved model, not use trainable flag
			fl=open(fname,"rb")
			nmodel = gensim.models.KeyedVectors.load_word2vec_format(fl, binary=True)
			fl.close()
			if(trainable):print("Load",fname,"as static word2vec model")
			staticmodels.append(nmodel)
		elif(trainable):#Saved Pickle object
			fl=open("MyModel.pickle","rb")
			nmodel = pickle.load(fl)
			fl.close()
			testKeys=model.__dict__.keys()
			if('predict_output_word' in testKeys and 'train' in testKeys and 'wv' in testKeys):
				trainablemodels.append(nmodel)
			else:
				raise Exception("Model \""+fname+"\" cannot used as trainable Word2Vec model")
		else:
			fl=open("MyModel.pickle","rb")
			nmodel = pickle.load(fl)
			fl.close()
			testKeys=model.__dict__.keys()
			if('predict_output_word' in testKeys and 'wv' in testKeys):
				staticmodels.append(nmodel)
			else:
				raise Exception("Model \""+fname+"\" cannot used as Word2Vec model")
	except Exception as e:
		print("Cannot load model",fname)
		print("Error:",e)

#extraModels=os.listdir(modelsPath+"extra/")
#for i in range(len(extraModels)):
#	extraModels[i]=modelsPath+extraModels[i]

print("Loading minimal necessary models...")

loadModel(modelsPath+"lemmed_n300.bin")
wordFormsModel=gensim.models.KeyedVectors.load_word2vec_format(open(modelsPath+"word_forms.bin","rb"), binary=True)
MyDict=gensim.corpora.dictionary.Dictionary.load(modelsPath+"words_dictionary.dct")
TfidfModel=gensim.models.tfidfmodel.TfidfModel.load(modelsPath+"words_tfidfmodel.tfdf")

print("Loaded")

def sentenceToTfidf(sent):
	'''
	Принимает лемматизированную строку или лист
	Возвращает словарь слово-важность.
	Ключ MaxImportant соответствует самому важному слову во входном массиве или строке
	'''
	if(type(sent)==str):sent=sent.split(" ")
	sent=MyDict.doc2bow(sent)
	sent=TfidfModel[sent]
	res=dict()
	mimp=""
	maxv=0
	for i,j in sent:
		res[MyDict[i]]=j
		if(j>maxv):
			maxv=j
			mimp=MyDict[i]
	res["MaxImportant"]=mimp
	return res

def NLP_lemm_addon_Tfidf(lemmed,arr=None):
	'''
	Обвязка для метода nlp.lemmatization. Добавляет в массив к каждому слову его важность
	Возвращает то же, что и nlp.lemmatization, но плюс к нему информацию TfiDf
	Возможен цепочный вызов по типу NLP_lemm_addon_Tfidf(nlp.lemmatization("съешь ещё этих булочек"))
	'''
	if(arr==None and type(lemmed)==tuple):
		lemmed,arr=lemmed
	tfidf_info=sentenceToTfidf(lemmed)
	for wi in range(len(arr)):
		if("pymorphy_nform" in arr[wi] and arr[wi]["pymorphy_nform"] in tfidf_info):
			arr[wi]["tfidf"]=tfidf_info[arr[wi]["pymorphy_nform"]]
	return lemmed,arr,tfidf_info

def wordsToMatrix(lemmed,weights=None,model=staticmodels[0],size=6):
	'''
	Преобразует лемматизированные слова в матрицу.
	Возвращает np.array с размерностью (size,размер вектора Word2Vec)
	lemmed -- лемматизированная строка
	weights -- веса слов, np.array или словарь. Если не задано, то вызывается sentenceToTfidf и применяется эти данные
	model -- используемая Word2Vec модель. По умолчанию staticmodels[0]
	size -- размер, до которого предложения будут сжаты/растянуты (в случае если число слов больше 6, то произойдёт потеря информации)
	'''
	words=lemmed
	if(type(lemmed)==str):
		words=lemmed.split(" ")
	if(type(weights)==type(None)):
		weights=sentenceToTfidf(lemmed)
	if(type(weights)==dict):
		tmp=np.zeros((len(words),))
		for i in range(len(words)):
			try:tmp[i]=weights[words[i]]
			except:pass
		weights=tmp
	res=np.zeros((size,model.wv.vector_size))
	weighted_vectors=[]
	for wi in range(len(words)):
		try:weighted_vectors.append(weights[wi]*model.wv.word_vec(words[wi])/np.linalg.norm(model.wv.word_vec(words[wi])))
		except:pass # Просто слово, которого нет в словаре, попалось
	znam=len(weighted_vectors)-1
	if(znam==0):
		for i in range(size):
			res[i]=weighted_vectors[0]/6;
		return res
	for wi in range(len(weighted_vectors)):
		firstInd=int(wi*(size-1)/znam)
		secondInd=firstInd+1
		firstWeight=1-(wi*(size-1)/znam-firstInd)
		res[firstInd]+=firstWeight*weighted_vectors[wi]
		if(1-firstWeight>1e-6):res[secondInd]+=(1-firstWeight)*weighted_vectors[wi]
	return res

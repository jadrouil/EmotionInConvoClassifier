from conversationExtract import * 
from naiveBayesInstance import *
import csv

def hotwordsTrain(hotwordsFile,naiveBayesCalculator):
	with open(hotwordsFile) as hotwordsF:
		hotWeight = int(hotwordsF.readline())
		for line in hotwordsF:
			word,emotion,bs = line.split()
			naiveBayesCalculator.train([instance(emotion, word)] * hotWeight)

def tweetTrain(bayesTrainFile, naiveBayesCalculator, emotionSet):
	for line in csv.reader(open(bayesTrainFile)):
		emo = line[0].lower()
		if emo not in emotionSet:
			continue
		sentence = line[1]
		for word in sentence:
			naiveBayesCalculator.train([instance(emo, word)])
def structuredConvosTrain(convos, emotionCC, emotions):
	for convo in convos:
		prevUsr1Emo = prevUsr2Emo = "START"
		for msg in convo:
			if msg.user() == 1:
				emotionCC.trainSent(msg.eTag(), prevUsr1Emo)
				emotionCC.trainReceive(msg.eTag(), prevUsr2Emo)
				prevUsr1Emo = msg.eTag()
			else:
				emotionCC.trainSent(msg.eTag(), prevUsr2Emo)
				emotionCC.trainReceive(msg.eTag(), prevUsr1Emo)
				prevUsr2Emo = msg.eTag()

def conversationTrain(conversationTrainfile, emotionCC, emotions):
	'''should train ecc'''
	conversations = conversationExtract(conversationTrainfile, emotions)
	structuredConvosTrain(
		convos = conversations,
		emotionCC = emotionCC,
		emotions = emotions)
	




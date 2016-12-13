from conversationExtract import * 
import csv

def hotwordsTrain(hotwordsFile,naiveBayesCalculator):
	with open(hotwordsFile) as hotwordsF:
		hotWeight = int(hotwordsF.readline())
		for line in hotwordsF:
			word,emotion,bs = line.split()
			naiveBayesCalculator.train([instance(emotion, word)] * hotWeight)

def tweetTrain(bayesTrainFile, naiveBayesCalculator, emotionSet):
	for line in csv.reader(open(bayesTrainFile)):
		emo = line[0]
		if emo not in emotionSet:
			continue
		sentence = line[1]
		for word in sentence:
			naiveBayesCalculator.train([instance(emo, word)])

def conversationTrain(conversationTrainfile, emotionCC, emotions):
	'''should train ecc'''
	conversations = conversationExtract(conversationTrainfile, emotions)
	for convo in conversations:
		prevUsr1Emo = prevUsr2Emo = "START"
		for msg in convo:
			if msg.user() == 1:
				emotionCC.trainSent(msg.eTag(), prevUsr1Emo)
				emotionCC.trainReceive(msg.eTag(), prevUsr2Emo)
				prevUsr1Emo = msg.eTag()
			else:
				emotionCC.trainSent(msg.eTag(), prevUsr2Emo)
				emotionCC.trainRecieve(msg.eTag(), prevUsr1Emo)
				prevUsr2Emo = msg.eTag()




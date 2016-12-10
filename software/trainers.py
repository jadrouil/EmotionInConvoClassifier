
import csv

def hotwordsTrain(hotwordsFile, hotWeight,naiveBayesCalculator):
	with open(hotwordsFile) as hotwordsF:
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
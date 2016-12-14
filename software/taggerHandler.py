from taggerFactory import *
from outputter import outputter
from accuracyTracking import accuracyTracker
from conversationExtract import *
from dataFolder import *
import sys


def noFold():
	emotionFile = sys.argv[1]
	conversationTrainfile = sys.argv[2]
	bayesTrainFile = sys.argv[3]
	hotwordsTrainFile = sys.argv[4]
	testfile = sys.argv[5]

	cet = createConversationEmotionTagger(emotionFile, conversationTrainfile, bayesTrainFile, hotwordsTrainFile)


	output = outputter(testfile)
	aT = accuracyTracker()

	for convo in conversationExtract(testfile, cet._emotions):
		result = cet.test(convo)
		output.write(result, convo)
		aT.compare(result, convo)

	print "Labeled emotions with ", aT.accuracy(), " percent accuracy."

def fold(numFolds = 5):
	emotionFile = sys.argv[1]
	conversationsFile = sys.argv[2]
	bayesTrainFile = sys.argv[3]
	hotwordsTrainFile = sys.argv[4]


	cet = createCETconvo(emotionFile, [], bayesTrainFile, hotwordsTrainFile)
	folder = dataFolder(conversationsFile, numFolds, cet._emotions)


	aT = accuracyTracker()
	for i in range(0, numFolds):
		print "FOLD NUMBER: ", i 
		aT.newFold()
		cet.resetECC(folder.train())
		output = outputter("convosFold" + str(i))

		for convo in folder.test():
			result = cet.test(convo)
			output.write(result, convo)
			aT.compareFold(result, convo)
		print "Labeled emotions for this fold ", aT.foldAccuracy(), " percent accuracy."

	print "Labeled emotions accross all folds ", aT.accuracy(), " percent accuracy."





if sys.argv[5].isdigit():
	fold(int(sys.argv[5]))
else:
	noFold()

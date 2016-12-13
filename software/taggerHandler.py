from taggerFactory import *
from extract import getConvo
from outputter import outputter
from accuracyTracking import accuracyTracker

import sys

emotionFile = sys.argv[1]
conversationTrainfile = sys.argv[2]
bayesTrainFile = sys.argv[3]
hotwordsTrainFile = sys.argv[4]
testfile = sys.argv[5]

cet = createConversationEmotionTagger(conversationTrainfile, bayesTrainFile, hotwordsTrainFile)


output = outputter(testfile)
aT = accuracyTracker()

with open(testfile) as testData:
	convo = getConvo(testData)
	while convo:
		result = cet.test(convo)
		output.write(result, convo)
		aT.compare(result, convo)
		convo = getConvo(testData)



print "Labeld emotions with ", aT.accuracy(), " percent accuracy."

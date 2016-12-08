from taggerFactory import *
from extract import getConvo
from outputter import outputter
from accuracyTracking import accuracyTracker

import sys


testfile = sys.argv[4]

conversationTrainfile = sys.argv[1]
bayesTrainFile = sys.argv[2]
hotwordsTrainFile = sys.argv[3]
cet = createConversationEmotionTagger(conversationTrainfile, bayesTrainFile, hotwordsTrainFile)


output = outputter(testfile)
aT = accuracyTracker()

with open(testfile) as testData:
	convo = getConvo(testData)
	while convo:
		result = cet.test(convo)
		output.write(result)
		aT.compare(result, convo)
		convo = getConvo(testData)



print "Labeld emotions with ", aT.accuracy(), " accuracy."

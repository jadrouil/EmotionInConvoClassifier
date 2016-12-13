from taggerFactory import *
from outputter import outputter
from accuracyTracking import accuracyTracker
from conversationExtract import *

import sys

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

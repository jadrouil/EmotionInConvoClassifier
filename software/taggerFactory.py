from trainers import *
from naiveBayeser import *
from emotionConnectionCalculator import *
from conversationEmotionTagger import *
#returns a fully trained emotion tagger
def createConversationEmotionTagger(emotionFile = "../datasets/emotions.txt", conversationTrainfile = "../datasets/conversations.txt", bayesTrainFile = "../datasets/bayesTrain.txt", hotwordsTrainFile = "../datasets/hotwords.txt", ):
	emotions = set([])
	with open(emotionFile) as emotionF:
		for line in emotionF:
			emotions.add(line.strip())


	naiveBayesCalculator = naiveBayeser()
	hotwordsTrain(hotwordsTrainFile, naiveBayesCalculator)
	tweetTrain(bayesTrainFile, naiveBayesCalculator, emotions)

	emotionCC = emotionConnectionCalculator()
	conversationTrain(conversationTrainfile, emotionCC, emotions)

	return conversationEmotionTagger(emotionCC, naiveBayesCalculator, emotions)



#refactor this to train the calculators directly
# def train(self, convo):
# 		'''takes conversation to train on'''
# 		user1previousEmotion = "START"
# 		user2previousEmotion = "START"
# 		for msg in convo:
# 			self._emotionConnectionCalculator.train(msg, user1previousEmotion, user2previousEmotion)
# 			self._emotionMessageCalculator.train(msg)
# 			if msg.user() == 1:
# 				user1previousEmotion = msg.eTag()
# 			else:
# 				user2previousEmotion = msg.eTag()

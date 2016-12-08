
#returns a fully trained emotion tagger
def createConversationEmotionTagger(emotionFile, conversationTrainfile , bayesTrainFile, hotwordsTrainFile, hotWeight = 50):
	emotions = set([])
	with open(emotionFile) as emotionF:
		for line in emotionF:
			emotions.add(line.strip())


	naiveBayesCalculator = naiveBayes()
	hotwordsTrain(hotwordsTrainFile, hotWeight, naiveBayesCalculator)
	tweetTrain(bayesTrainFile, naiveBayesCalculator, emotions)

	emotionCC = emotionConnectionCalculator()
	conversationTrain(conversationTrainfile, emotionCC, emotions)


def hotwordsTrain(hotwordsFile, hotWeight,naiveBayesCalculator):
	with open(hotwordsFile) as hotwordsF:
		for line in hotwordsF:
			word,emotion,bs = line.split()
			naiveBayesCalculator.train([instance(emotion, word)] * hotWeight)


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

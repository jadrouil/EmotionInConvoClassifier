def createConversationEmotionTagger(trainfile = ""):
	'''returns ConversationEmotionTagger trained on trainfile or untrained if not specified'''

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

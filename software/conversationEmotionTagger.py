'''
I will create a factory for this class so you can simply call createConversationEmotionTagger()
since I will have to modifiy the __init__ function
'''

class conversationEmotionTagger:


	def __init__(self):
		'''takes a conversation as input and outputs a tagged conversation'''


	def test(self, convo):
		'''takes a convo and returns a labeled predicition
		does not require an eTagged input'''
	def train(self, convo):
		'''takes conversation to train on'''
		user1previousEmotion = "START"
		user2previousEmotion = "START"
		for msg in convo:
			self._emotionConnectionCalculator.train(msg, user1previousEmotion, user2previousEmotion)
			self._emotionMessageCalculator.train(msg)
			if msg.user() == 1:
				user1previousEmotion = msg.eTag()
			else:
				user2previousEmotion = msg.eTag()

'''
I will create a factory for this class so you can simply call createConversationEmotionTagger()
since I will have to modifiy the __init__ function
'''

class conversationEmotionTagger:


	def __init__(self, emotionConnectionCalculator, emotionMessageCalculator):
		'''takes a conversation as input and outputs a tagged conversation'''
		self._emotionConnectionCalculator = emotionConnectionCalculator
		self._emotionMessageCalculator = emotionMessageCalculator

	def test(self, convo):
		'''takes a convo and returns a labeled predicition
		does not require an eTagged input'''


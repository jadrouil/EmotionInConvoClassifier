'''
I will create a factory for this class so you can simply call createConversationEmotionTagger()
since I will have to modifiy the __init__ function
'''
from ViterbiTable import ViterbiTable

class conversationEmotionTagger:


	def __init__(self, emotionConnectionCalculator, emotionMessageCalculator, emotions):
		'''takes a conversation as input and outputs a tagged conversation'''
		self._emotionConnectionCalculator = emotionConnectionCalculator
		self._emotionMessageCalculator = emotionMessageCalculator
		self._emotions = emotions

	def test(self, convo):
		prevSent = prevRecv = -1
		vTable = ViterbiTable(convo, emotions)
		lastUser1Index, lastUser2Index = vTable.initialize(self._emotionConnectionCalculator, self._emotionMessageCalculator)
		vTable.iterate( astUser1Index, lastUser2Index, self._emotionConnectionCalculator, self._emotionMessageCalculator)
		labeledConversation = vTable.sequence()
		return labeledConversation
from collections import defaultdict
import math

class emotionConnectionCalculator:
	def __init__(self):
		'''allows you to calculate the probability of an emotion
		 given the previous sentt and received messages'''
		self._countSentEmotion = defaultdict(lambda: defaultdict(lambda: 0.0))
		self._countRecvEmotion = defaultdict(lambda: defaultdict(lambda: 0.0))
		self._totalSentEmotion = defaultdict(lambda: 0.0)
		self._totalRecvEmotion = defaultdict(lambda: 0.0)

	def trainSent(self, emotion, prevSentEmotion):
		self._countSentEmotion[prevSentEmotion][emotion] += 1.0
		self._totalSentEmotion[prevSentEmotion] += 1.0

	def trainReceive(self, emotion, prevRecvEmotion):
		self._countRecvEmotion[prevRecvEmotion][emotion] += 1.0
		self._totalRecvEmotion[prevRecvEmotion] += 1.0

	def pGivenSent(self, emotion, prevSentEmotion):
		return math.log((self._countSentEmotion[prevSentEmotion][emotion] + 1.0) / (self._totalSentEmotion[prevSentEmotion] + len(self._countSentEmotion[prevSentEmotion])))
	def pGivenReceived(self, emotion, prevRecvEmotion):
		return math.log((self._countRecvEmotion[prevRecvEmotion][emotion]  + 1.0)/ (self._totalRecvEmotion[prevRecvEmotion] + len(self._countRecvEmotion[prevRecvEmotion]) ))
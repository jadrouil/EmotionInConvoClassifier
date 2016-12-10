from naiveBayesInstance import *

class ViterbiTable:
	def __init__(self, convo, emotions):
		self._convo = convo
		self._emotions = list(emotions)
		self._table = []
		assert(convo)

	def initialize(self, ecc, emc):
		self._table.append(ViterbiCell())
		self._table.append(ViterbiCell())
		
		user1msgIndex = 0
		for i in range(0, len(self._emotions)):
			inst = instance(None, self._convo[0].content)
			pEmotion = emc.test(inst, self._emotions[i])
			pEmotionSent = ecc.pGivenSent(self._emotions[i], "START")
			pEmotionRecv = ecc.pGivenReceived(self._emotions[i], "START")
			self._table[0].addRowToCell(pEmotion + pEmotionSent + pEmotionRecv, -1)

		user2msgindex = 1
		for i in range(0, len(self._emotions)):
			inst = instance(None, self._convo[1].content)
			pEmotion = emc.test(inst, self._emotions[i])
			pEmotionSent = ecc.pGivenSent(self._emotions[i], "START")
			pEmotionRecv = self._maximizingRecvP(ecc)
			self._table[0].addRowToCell(pEmotion + pEmotionSent + pEmotionRecv, -1)
		return user1msgIndex,user2msgindex

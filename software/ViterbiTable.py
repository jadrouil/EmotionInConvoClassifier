from naiveBayesInstance import *

class ViterbiTable:
	def __init__(self, convo, emotions):
		self._convo = convo
		self._emotions = list(emotions)
		self._table = []
		assert(convo)

	def _traceLabel(self, tracingUser, lastEmotionIndex, emotionLabels):
		for i in range(len(self._convo) - 1, -1):
			if self._convo[i].user() == tracingUser:
				emotionLabels[i] = self._emotions[lastEmotionIndex]
				lastEmotionIndex = self._table[i].backptr(lastEmotionIndex)
	
	def _selectMaximizingRecvP(self, ecc, lastRecvIndex, emotion):
		psForEmotionRecv = [ecc.pGivenReceived(prevE, emotion) for prevE in self._emotions]
		return max(psForEmotionRecv)
	
	def _selectMaxCombo(self, lastSentIndex, lastRecvIndex, emotion, ecc):
		maxP = None
		backptr = None
		for i in range(0, len(self._emotions)):
			sentProb = self._table[lastSentIndex].score()
			pGivenSent = ecc.pGivenSent(emotion, self._emotions[i]) 
			for j in range(0, len(self._emotions)):
				recvProb = self._table[lastSentIndex].score()
				pGivenRecv = ecc.pGivenReceived(emotion, self._emotions[j])
				totalP = sentProb + pGivenSent + recvProb + pGivenRecv 
				if totalP > maxP:
					maxP = totalP
					backptr = i
		return maxP, backptr

	def _fillCell(self, vCell, lastSentIndex, lastRecvIndex, msg, emc, ecc):
		for i in range(0, len(self._emotions)):
			pEmotion = emc.test(msg, self._emotions[i])
			maxP, backptr = self._selectMaxCombo(lastSentIndex, lastRecvIndex,self._emotions[i], ecc)
			vCell.addRowToCell(pEmotion + maxP, backptr)

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

		user2msgIndex = 1
		for i in range(0, len(self._emotions)):
			inst = instance(None, self._convo[1].content)
			pEmotion = emc.test(inst, self._emotions[i])
			pEmotionSent = ecc.pGivenSent(self._emotions[i], "START")
			pEmotionRecv = self._maximizingRecvP(ecc, user1msgIndex)
			self._table[0].addRowToCell(pEmotion + pEmotionSent + pEmotionRecv, -1)
		return user1msgIndex,user2msgIndex


	def iterate(self, user1msgIndex,user2msgIndex, ecc, emc):
		for i in range(2, len(self._convo)):
			newCell = ViterbiCell()
			msg = instance(self._convo[i].content())
			if self._convo[i].user() == 1:
				self._fillCell(newCell, user1msgIndex, user2msgIndex, msg, emc, ecc)
				user1msgIndex = i
			else:
				self._fillCell(newCell, user2msgIndex, user1msgIndex, msg, emc, ecc)
				user2msgIndex = i
			self._table.append(newCell)

	def sequence(self):
		emotionLabels = [None] * len(self._convo)
		emotionIndex = self._selectMostLikely(self._table[-1])
		lastEmotionIndex = self._table[-1].backptr(emotionIndex)
		emotionLabels[-1] = self._emotions[emotionIndex]
		tracingUser = self._convo[-1].user()
		
		self._traceLabel(tracingUser, lastEmotionIndex, emotionLabels)

		for i in range(len(self._convo) - 1, -1):
			if self._convo[i].user() != tracingUser:
				emotionIndex = self._selectMostLikely(self._table[i])
				lastEmotionIndex = self._table[i].backptr(emotionIndex)
				emotionLabels[i] = self._emotions[emotionIndex]
				tracingUser = self._convo[i].user()
				break
		self._traceLabel(tracingUser, lastEmotionIndex, emotionLabels)
		return emotionLabels
		
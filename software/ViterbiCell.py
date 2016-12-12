
class ViterbiCell:
	def __init__(self):
		self.scoresAndPtrs = []
	def selectMostLikely(self):
		mostLikelyIndex = None
		mostLikelyP = None
		for i in range(0, len(self.scoresAndPtrs)):
			if mostLikelyP < self.scoresAndPtrs[i][0]:
				mostLikelyP = self.scoresAndPtrs[i][0]
				mostLikelyIndex = i
		return mostLikelyIndex
	def addRowToCell(self, score, backptr):
		self.scoresAndPtrs.append((score, backptr))
	def backptr(self, index):
		return self.scoresAndPtrs[index][1]
	def score(self, index):
		return self.scoresAndPtrs[index][0]
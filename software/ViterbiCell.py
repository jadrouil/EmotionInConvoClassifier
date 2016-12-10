

class ViterbiCell:
	def __init__(self):
		self.scoresAndPtrs = []

	def addRowToCell(self, score, backptr):
		self.scoresAndPtrs.append((score, backptr))
	def backptr(self, index):
		return self.scoresAndPtrs[index][1]
	def score(self, index):
		return self.scoresAndPtrs[index][0]
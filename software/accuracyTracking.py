
class accuracyTracker:
	def __init__(self):
		self._total = 0.0
		self._right = 0.0

	def compare(self, result, convo):
		assert(len(result) == len(convo))

		for i in range(0, len(result)):
			if result[i] == convo[i].eTag():
				self._right += 1.0
			self._total += 1.0
	def accuracy(self):
		return self._right / self._total * 100

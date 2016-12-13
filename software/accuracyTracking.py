from collections import defaultdict
class accuracyTracker:
	def __init__(self):
		self._totalForEmotion = defaultdict(lambda: 0.0)
		self._rightForEmotion = defaultdict(lambda: 0.0)

	def compare(self, result, convo):
		assert(len(result) == len(convo))

		for i in range(0, len(result)):
			if result[i] == convo[i].eTag():
				self._rightForEmotion[convo[i].eTag()] += 1.0
			self._totalForEmotion[convo[i].eTag()] += 1.0
	def accuracy(self):
		results = []
		for emotion, numCorrect in self._rightForEmotion.items():
			results.append((emotion, numCorrect / self._totalForEmotion[emotion] * 100))
		return results
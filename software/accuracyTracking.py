from collections import defaultdict
def formResults(emotionsRight, emotionsTotal):
	results = []
	for emotion, total in emotionsTotal.items():
		results.append((emotion, emotionsRight[emotion] / total  * 100))
	return results



class accuracyTracker:
	def __init__(self):
		self._totalForEmotion = defaultdict(lambda: 0.0)
		self._rightForEmotion = defaultdict(lambda: 0.0)
		self._totalForEmotionFold = defaultdict(lambda: 0.0)
		self._rightForEmotionFold = defaultdict(lambda: 0.0)

	def compare(self, result, convo):
		assert(len(result) == len(convo))

		for i in range(0, len(result)):
			if result[i] == convo[i].eTag():
				self._rightForEmotion[convo[i].eTag()] += 1.0
			self._totalForEmotion[convo[i].eTag()] += 1.0
	def accuracy(self):
		return formResults(self._rightForEmotion, self._totalForEmotion)
		

	def foldAccuracy(self):
		return formResults(self._rightForEmotionFold, self._totalForEmotionFold)

	def newFold(self):
		for emo, count in self._totalForEmotionFold.items():
			self._totalForEmotion[emo] += count
		self._totalForEmotionFold = defaultdict(lambda: 0.0)

		for emo, count in self._rightForEmotionFold.items():
			self._rightForEmotion[emo] += count
		self._rightForEmotionFold = defaultdict(lambda: 0.0)

	def compareFold(self, result, convo):
		assert(len(result) == len(convo))

		for i in range(0, len(result)):
			if result[i] == convo[i].eTag():
				self._rightForEmotionFold[convo[i].eTag()] += 1.0
			self._totalForEmotionFold[convo[i].eTag()] += 1.0

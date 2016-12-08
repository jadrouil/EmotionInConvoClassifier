
def hotwordsTrain(hotwordsFile, hotWeight,naiveBayesCalculator):
	with open(hotwordsFile) as hotwordsF:
		for line in hotwordsF:
			word,emotion,bs = line.split()
			naiveBayesCalculator.train([instance(emotion, word)] * hotWeight)
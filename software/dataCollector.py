from collections import defaultdict
import math
calculateLogBayesProb = lambda currentLogSum, nextProbability: currentLogSum + math.log(nextProbability)
#Jeremy Drouillard jadrouil


class dataCollector:
	def __init__(self):
		'''used to calculate probabilities for naive bayes'''
		self._totalInstanceCount = 0.0
		self._countOfSense = defaultdict(lambda: 0.0)

		self._occurencesOfFeatureForSense = defaultdict(lambda: defaultdict(lambda: 0.0))
		self._numFeaturesForSense = defaultdict(lambda: 0.0)
	def _probSense(self, sense):
		return self._countOfSense[sense] / self._totalInstanceCount
	def _probFeatureGivenSense(self, feat, sense):
		return (self._occurencesOfFeatureForSense[sense][feat] + 1.0) / (self._numFeaturesForSense[sense] + len(self._occurencesOfFeatureForSense[sense]))
	def add(self, instance):
		self._totalInstanceCount += 1.0
		self._countOfSense[instance.emotion] += 1.0

		for feature in instance.context:
			self._numFeaturesForSense[instance.emotion] += 1.0
			self._occurencesOfFeatureForSense[instance.emotion][feature] += 1.0
	def calcProb(self, sense, instance):
		probabilityOfFeatureGivenSense = [self._probFeatureGivenSense(feat, sense) for feat in instance.context]
		probabilityOfSense = reduce(calculateLogBayesProb, probabilityOfFeatureGivenSense, math.log(self._probSense(sense)))
		return probabilityOfSense

	def possibleSenses(self):
		return self._countOfSense.keys()
import string

class instance:
	def __init__(self, emotion, context):
		if emotion:
			self.emotion = emotion.lower()
		context = context.lower()
		for c in string.punctuation:
			context = context.replace(c, "")
		self.context = context.split()
		

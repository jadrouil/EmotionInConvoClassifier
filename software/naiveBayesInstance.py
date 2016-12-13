#Jeremy Drouillard jadrouil

class instance:
	def __init__(self, emotion, context):
		if emotion:
			self.emotion = emotion.lower()
		self.context = context.split()
		

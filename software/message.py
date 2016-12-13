
#a conversation will just be a list of messages
class message:
	'''container for data that will be used by algorithm to label emotion'''
	def __init__(self, content, eTag, userId):
		self._content = content
		self._eTag = eTag.lower()
		assert(userId in (1,2))
		self._userId = userId #possible values are 1 or 2

	def user(self):
		return self._userId
	def eTag(self):
		return self._eTag
	def content(self):
		return self._content



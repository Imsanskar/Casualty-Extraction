import nltk

class Tagger:
	"""
		Class for POS tagging of the sentences
	"""
	def __init__(self, sentences):
		self.sentences = sentences
		self.tags = [nltk.pos_tag(sentence) for sentence in sentences]

	def getTaggedSentences(self):
		"""
			Returns the pos_tagged sentences, pos tagging is don using nltk
		"""
		return self.tags
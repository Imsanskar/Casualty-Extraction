import nltk

"""
	Class for POS tagging of the sentences
	Input:
		sentences: Tokenized sentences
"""
class Tagger:
	
	def __init__(self, sentences):
		self.sentences = sentences
		self.tags = [nltk.pos_tag(sentence) for sentence in sentences]

	def getTaggedSentences(self):
		"""
			Returns the pos_tagged sentences, pos tagging is done using nltk
		"""
		return self.tags
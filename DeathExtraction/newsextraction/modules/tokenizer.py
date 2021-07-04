import nltk

class Tokenize:
	"""
		Tokenize the given paragraph. Here the tokenization is done using nltk library
	"""
	def __init__(self, paragraph):
		self.paragraph = paragraph
		self.sentences = nltk.sent_tokenize(self.paragraph)
		self.words = [nltk.word_tokenize(sentence) for sentence in self.sentences]

	def sentenceTokenize(self):
		"""
			Returns: sentence token of the given paragraph
		"""
		return nltk.sent_tokenize(self.paragraph)

	def wordTokenize(self):
		"""
			Returns: word token of the given paragraph
		"""
		return self.words

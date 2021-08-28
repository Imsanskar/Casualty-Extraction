import nltk
import datetime
import re

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

	def get_date(self,complete_news):
		date_regex = r'([0-9]{4}/[0-9]{2}/[0-9]{2})'
		contains_date = complete_news

		# #
		if contains_date[0] == '\n':
			contains_date = contains_date[1:]
		matches = re.search(date_regex, contains_date)
		# print (matches.group(1).strip())
		if matches is None:
			return ""
		date = datetime.datetime.strptime(matches.group(1).strip(), "%Y/%m/%d")
		month,year, date = date.month, date.year, matches.group(1).strip()

		return date
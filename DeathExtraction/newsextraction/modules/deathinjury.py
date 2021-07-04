"""
	Extract death and injury from the sentence list
	Compare with the death and injury verb to select the
	perfect predicate.
"""

from nltk.stem import WordNetLemmatizer
from transformers.file_utils import TOKENIZERS_IMPORT_ERROR
from wordNum import *
from transformers import BigBirdForQuestionAnswering
import tokenizer

def death_no(sentlist):
	# instance for lemmatizer
	lemmatizer = WordNetLemmatizer()

	# comparision verbs
	deathverb = ['die', 'kill', 'crush', 'pass']
	injuryverb = ['injure', 'sustain', 'critical', 'hurt', 'wound', 'harm', 'trauma']
	verbs = []
	death = "None"
	model = BigBirdForQuestionAnswering.from_pretrained("google/bigbird-base-trivia-itc")
	question = "died"
	context = sentlist[0]
	encoded_input = tokenizer(question, context, return_tensors='pt')
	death = model(**encoded_input)

	return convertNum(death)


def convertNum(toconvert:str) -> int:
	toconvert = toconvert.lower()
	intconvert = text2int(toconvert)
	if intconvert.split() == toconvert.split():
		death_no = 1
	else:
		checklist = intconvert.split(" ")
		# print(checklist)
		deathdigit = [int(s) for s in intconvert.split() if s.isdigit()]
		# print(deathdigit)
		for i in deathdigit:
			if i > 1900:
				point = checklist.index(str(i))
				checklist = checklist[point + 1:]
				dpoint = deathdigit.index(i)
				deathdigit = deathdigit[dpoint + 1:]
				# print(checklist)
				break
		if deathdigit == []:
			death_no = 1
		else:
			death_no = deathdigit[0]
	return death_no




def remove_date(toremove:str) -> str:
	"""
		Removes the date from the text
		News articles coming from sources contains date of news published in the beginning of
		the first sentence. Due to this POS tagging doesn’t work as it should so before extracting
		day, vehicles number, vehicles involved, etc. the date is extracted and removed from the
		news article.
		Input: 
			toremove: text from which date is to be removed
		Returns:
			Text with date removed
	"""
	toremove = toremove.replace('- ', ' ')
	checklist = toremove.split(" ")
	# print(checklist)
	deathdigit = [int(s) for s in toremove.split() if s.isdigit()]
	if deathdigit == []:
		value = checklist
	else:
		# print(deathdigit)
		for i in deathdigit:
			if i > 1900:
				point = checklist.index(str(i))
				checklist = checklist[point + 1:]
				deathdigit = deathdigit[point + 1:]
				# print(checklist)
				break
		value = checklist
	value = (" ").join(value)
	return value
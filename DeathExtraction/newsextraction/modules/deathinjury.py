"""
	Extract death and injury from the sentence list
	Compare with the death and injury verb to select the
	perfect predicate.
"""
import torch
from nltk.stem import WordNetLemmatizer
from .wordNum import *
from transformers import pipeline


question_answerer = pipeline('question-answering')


def death_no(news, header):
	# instance for lemmatizer
	lemmatizer = WordNetLemmatizer()

	# comparision verbs
	deathverb = ['died', 'killed', 'crushed', 'passed', 'die', 'kill', 'dead']

	if len(news) > 100:
		context = news[:100]
	else:
		context = news
	
	score = 0
	answer = ""
	for verb in deathverb:
		if verb in header:
			death = question_answerer(
				{
					'question': 'How many people died?',
					'context': header
				}
			)
			if death['score'] > score:
				score = death['score']
				answer = death['answer']


		# only calculate the score if the verb is in the context
		if verb not in context:
			continue
		death = question_answerer(
			{
				'question': 'How many people ' + verb + '?',
				'context': context
			}
		)
		if death['score'] > score:
			score = death['score']
			answer = death['answer']
	
	return answer


def injury_no(news, header):
	injuryverb = ['injure', 'sustain', 'critical', 'hurt', 'wound', 'harm', 'trauma']
	verbs = []
	death = "None"
	question = "died"
	
	
	if len(news) > 150:
		context = news[:150]
	else:
		context = news


	score = 0
	answer = ""
	injury = question_answerer(
		{
			'question': 'How many people ' + died + '?',
			'context': context
		}
	)
	for verb in injuryverb:
		# if verb in header:
		# 	injury = question_answerer(
		# 		{
		# 			'question': 'How many people died?',
		# 			'context': header
		# 		}
		# 	)
		# 	if injury['score'] > score:
		# 		score = injury['score']
		# 		answer = injury['answer']
		# only calculate the score if the verb is in the context
		if verb not in context:
			continue
		injury = question_answerer(
			{
				'question': 'How many people ' + verb + '?',
				'context': context
			}
		)
		if injury['score'] > score:
			score = injury['score']
			answer = injury['answer']
	
	return answer


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
import spacy
import en_core_web_sm

from spacy.matcher import Matcher
from spacy.attrs import POS,LOWER,IS_PUNCT,LEMMA

nlp = en_core_web_sm.load()


vehicles = ['bus','car','truck','tripper','bike','jeep','zeep','scooter','scooty',
		'motorbike','motorcycle','container','SUV','tractor','moped','lorry',
		'minivan','minibus','trolley','tempo','cycle']
three_wheeler=set([
'tempo','three-wheeler','three wheeler'
])

two_wheeler = set([
'bike','scooter','scooty','motorbike','motorcycle','two-wheeler','two wheeler','moped','cycle'
])

four_wheeler = set([
'bus','car','truck','tripper','zeep','jeep','container','SUV','tractor','moped','lorry',
'minivan','minibus','trolley','four-wheeler','four wheeler',
])

scooty = ['scooty','scooter']
bike = ['bike','motorbike','motorcycle']
zeep = ['jeep','zeep']
matcher = Matcher(nlp.vocab)


class VehicleInformation:
	def __init__(self,news_story):
		self.news_story = news_story


	def make_gazetter(self):
		for vehicle in vehicles:
			matcher.add("Vehicles", [[{LEMMA:vehicle}]])
		matcher.add("Vehicles", [[{LEMMA:'two'},{IS_PUNCT:True},{LEMMA:'wheeler'}]])
		matcher.add("Vehicles", [[{LEMMA:'two'},{LEMMA:'wheeler'}]])
		matcher.add("Vehicles", [[{LEMMA:'four'},{IS_PUNCT:True},{LEMMA:'wheeler'}]])
		matcher.add("Vehicles", [[{LEMMA:'four'},{LEMMA:'wheeler'}]])

	def find_vehicles(self):
		"""
			Returns the types of vehicles
		"""
		vehicles_found = set()
		document = self.news_story
		doc = nlp(document)
		# matcher = Matcher(nlp.vocab)
		is_four_wheeler=is_three_wheeler=is_two_wheeler = 0

		self.make_gazetter()
		matches = matcher(doc)
		for ent_id, start, end in matches:
			vehicles_found.add(doc[start:end].text)
		if(len(vehicles_found.intersection(two_wheeler))!=0):
			is_two_wheeler = 1
		if(len(vehicles_found.intersection(three_wheeler))!=0):
			is_three_wheeler = 1
		if(len(vehicles_found.intersection(four_wheeler))!=0):
			is_four_wheeler = 1

		
		returnString = ""
		for v in vehicles_found:
			returnString += "," + v
		return(returnString[1:],is_two_wheeler,is_three_wheeler,is_four_wheeler, len(vehicles_found))
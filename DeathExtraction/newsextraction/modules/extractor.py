#TODO: create a class called DataExtractor to extract key information from the given news
from .tagger import Tagger
from .tokenizer import Tokenize
import nltk
import re
from newsextraction.modules.locationTree import LocationInformation
import spacy
nlp = spacy.load('en_core_web_lg')

class DataExtractor:
	def __init__(self, posTaggedSentences, newsStory: str,title):
		"""
			Constructor for the Data extractor class
			Initializes the object
		"""
		self.title = title
		self.news = newsStory
		self.posTaggedSentences = posTaggedSentences

	
	def get_title_location_chunks(self):
		"""
		extract the location i.e label == GPE means location
		"""
		gpe=[]
		doc = nlp(str(self.title))
		for ent in doc.ents:
			if (ent.label_ == 'GPE'):
				gpe.append(ent.text)

		return gpe

	def get_body_location_chunks(self):

		"""
		extract the location i.e label == GPE means location
		"""
		gpe=[]
		doc = nlp(str(self.news))
		for ent in doc.ents:
			if (ent.label_ == 'GPE'):
				gpe.append(ent.text)

		return gpe
		
	def getLocation(self) :
		"""
			Returns the location where the accident had happened
			At first we parse title to search for location , if location not found in title then we search in body
		"""
		locations =[]
		locations=self.get_title_location_chunks()
		if len(locations) != 0:
			print(locations)
			return locations[0]
		locations.extend(self.get_body_location_chunks())


		return_value = locations
		
		ktm_location = LocationInformation().all_ktm_locations()
		bkt_location = LocationInformation().all_bkt_locations()
		ltp_location = LocationInformation().all_ltp_locations()
		outside_location = LocationInformation().all_locations()
		all_locations = ktm_location + outside_location + bkt_location + ltp_location

		locations_final = return_value
		return_location = []
		max_ratio = 0
		max_location = []

		"""
		here we match and verify the location according to the one stored in our location tree.
		"""

		for glocation in locations_final:
			for location in all_locations:
				dist = nltk.edit_distance(glocation, location)
				ratio = (1 - (dist / len(glocation))) * 100
				max_ratio = max(max_ratio, ratio)
				if max_ratio >= 70:
					max_location = location
					if max_ratio == ratio:
						if max_location in ktm_location:
							return_location = max_location
						elif max_location in ltp_location:
						 	return_location = max_location
						elif max_location in bkt_location:
						 	return_location = max_location
						elif max_location in outside_location:
						 	return_location = max_location
			print("return_location:", return_location )

		return return_location
	
	def getDay(self, complete_news):
		""" Gets the day of mishap.
		"""
		day_regex = re.compile('\w+day')
		day = day_regex.findall(complete_news)[0]
		return day

	def vehicle(self):
		""" Gets the vehicle number from the news story.
			Inputs include the POS tagged words from the news.
			Output is the phrase containing the vehicle number.
		"""
		vehicle_regex = "Vehicle: {<.*><CD><.*><CD>}"
		vehicle_parser = nltk.RegexpParser(vehicle_regex)

		vehicles = []
		for i in self.posTaggedSentences:
			vehicle = vehicle_parser.parse(i)
			for i in vehicle.subtrees(filter=lambda x: x.label() == 'Vehicle'):
				vehicle = ""
				for p in i.leaves():
					vehicle = vehicle + str(p[0]) + " "
				vehicles.append(vehicle[:-1])

		returnString = ""
		for v in vehicles:
			returnString += "," + v

		return returnString[1:]
	
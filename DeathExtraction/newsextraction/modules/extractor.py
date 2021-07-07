#TODO: create a class called DataExtractor to extract key information from the given news
from .tagger import Tagger
from .tokenizer import Tokenize
import nltk
from newsextraction.modules.locationTree import LocationInformation

class DataExtractor:
	def __init__(self, posTaggedSentences, newsStory: str,title):
		"""
			Constructor for the Data extractor class
			Initializes the object
		"""
		self.title = title
		self.news = newsStory
		self.posTaggedSentences = posTaggedSentences

		
	def getLocation(self) :
		"""
			Returns the location where the accident had happened
			At first we parse title to search for location , if location not found in title then we search in body
		"""

		#search in title
		title_sentences = nltk.sent_tokenize(str(self.title).encode('ascii', errors='ignore').decode("utf-8"))
		locations =[]

		for sent in title_sentences:
			words = nltk.word_tokenize(sent)
			if ("died" or "death" or "injured" or "injury" or "injuries" or "killed" or "casualty" or "accident" or "crash" or "crashed" or "collided" or "hit" or "lost" ) in words:
				#grouping similar kinds of words (name_entities)
				chunked_sentence = nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent)))
				#label:GPE holds data for location in chunked_sentences
				for i in chunked_sentence.subtrees(filter=lambda x: x.label() == 'GPE'):
					print(i)
					for i in i.leaves():
						locations.append(i[0])

		if len(locations) != 0:
			print("after extracting all locations : " + str(locations))
			
		else:


			individual_sentences = nltk.sent_tokenize(str(self.news).encode('ascii', errors='ignore').decode("utf-8"))


			for sent in individual_sentences:
				words = nltk.word_tokenize(sent)
				if ("died" or "death" or "injured" or "injury" or "injuries" or "killed" or "casualty" or "accident" or "crash" or "crashed" or "collided" or "hit" or "lost" ) in words:
					#grouping similar kinds of words (name_entities)
					chunked_sentence = nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent)))
					#label:GPE holds data for location in chunked_sentences
					for i in chunked_sentence.subtrees(filter=lambda x: x.label() == 'GPE'):
						print(i)
						for i in i.leaves():
							locations.append(i[0])
			

		return_value = locations

			

		
		try:
				if (locations[0] == "New") or (locations[0] == "Old"):
					return_value = []
					return_value.append(locations[0] + " " + locations[1])
		except:
				pass

		

		
		ktm_location = LocationInformation().all_ktm_locations()
		bkt_location = LocationInformation().all_bkt_locations()
		ltp_location = LocationInformation().all_ltp_locations()
		outside_location = LocationInformation().all_locations()
		all_locations = ktm_location + outside_location + bkt_location + ltp_location

		locations_final = return_value
		return_location = []
		max_ratio = 0
		max_location = []

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

		return return_location
	
	def getDate(self, sentences):
		""" Gets the number of deaths from the news story.
			Inputs include the POS tagged words from the news story.
			Output includ the number of deaths mentioned in the news.
		"""
		death_words = ["died", "death", "killed", "life"]
		# death_regex = "Deaths: {<NNP>?<CD><NNS|NNP>?<VBD|VBN>?<VBD|VBN>}"
		death_regex = "Deaths: {<CD>}"
		has_deaths = [sent for sent in sentences if ("died" or "death") in nltk.word_tokenize(sent)]
	
		death_parser = nltk.RegexpParser(death_regex)

		for i in self.posTaggedSentences:
			deaths = death_parser.parse(i)
			for i in deaths.subtrees(filter=lambda x: x.label() == 'Deaths'):
				# print(i.leaves())
				pass
	
	def getDeathNumber(self):
		raise NotImplementedError
	
	def getInjuryNumber(self):
		raise NotImplementedError
	
from transformers import pipeline
import nltk


try:
	nltk.data.find('tokenizers/punkt')
except LookupError:
	nltk.data.find('tokenizers/averaged_perceptron_tagger')
	nltk.download("punkt")


# try:
# 	nltk.data.find('tokenizers/averaged_perceptron_tagger')
# except LookupError:
# 	nltk.download('averaged_perceptron_tagger')

question_answerer = pipeline('question-answering')
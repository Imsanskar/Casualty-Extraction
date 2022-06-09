from transformers import pipeline
import nltk


try:
	nltk.data.find('tokenizers/punkt')
except LookupError:
	nltk.download("punkt")
	nltk.download('averaged_perceptron_tagger')


# try:
# 	nltk.data.find('tokenizers/averaged_perceptron_tagger')
# except LookupError:

question_answerer = pipeline('question-answering')
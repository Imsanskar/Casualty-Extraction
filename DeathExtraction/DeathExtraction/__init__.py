from transformers import pipeline
import nltk

question_answerer = pipeline('question-answering')

try:
	nltk.data.find('tokenizers/punkt')
except LookupError:
	nltk.download("punkt")


try:
	nltk.data.find('tokenizers/punkt')
except LookupError:
	nltk.download('averaged_perceptron_tagger')
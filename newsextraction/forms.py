
from django import forms
class NameForm(forms.Form):
	"""
	input: news link youu wnat to manually extract
	"""
	news_link = forms.CharField(max_length=500, label='News Link', widget=forms.TextInput(attrs={'class':'form-control', 'id':"newsLinkForm", 'placeholder':'Search'}))
	isSave = forms.BooleanField(required=False)


class SearchForm(forms.Form):
	"""
	form for creating the search form including all the checkboxes to query the search
	"""
	all = forms.BooleanField(widget=forms.CheckboxInput(),initial=True,required=False) # initially search in all fields
	header = forms.BooleanField(widget=forms.CheckboxInput(),required=False)
	body = forms.BooleanField(widget=forms.CheckboxInput(),required=False)
	source = forms.BooleanField(widget=forms.CheckboxInput(),required=False)
	location = forms.BooleanField(widget=forms.CheckboxInput(),required=False)
	death_no = forms.BooleanField(widget=forms.CheckboxInput(),required=False)
	injury_no = forms.BooleanField(widget=forms.CheckboxInput(),required=False)
	date = forms.BooleanField(widget=forms.CheckboxInput(),required=False)
	year = forms.BooleanField(widget=forms.CheckboxInput(),required=False)
	month = forms.BooleanField(widget=forms.CheckboxInput(),required=False)
	day = forms.BooleanField(widget=forms.CheckboxInput(),required=False)

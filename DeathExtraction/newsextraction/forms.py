
from django import forms
class NameForm(forms.Form):
    """
    input: news link youu wnat to manually extract
    """
    news_link = forms.CharField(max_length=500, label='News Link', widget=forms.TextInput(attrs={'class':'form-control', 'id':"newsLinkForm", 'placeholder':'Search'}))



class SearchForm(forms.Form):
	"""
	For search form, we create checkboxes for searching in different entities of database. 
	"""
	all = forms.BooleanField(widget=forms.CheckboxInput(),initial=True,required=False)
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

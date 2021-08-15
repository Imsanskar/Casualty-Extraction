
from django import forms
class NameForm(forms.Form):
    """
    input: news link youu wnat to manually extract
    """
    news_link = forms.CharField(max_length=500, label='News Link', widget=forms.TextInput(attrs={'class':'form-control', 'id':"newsLinkForm", 'placeholder':'Search'}))
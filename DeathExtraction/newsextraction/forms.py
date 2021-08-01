
from django import forms
class NameForm(forms.Form):
    """
    input: news link youu wnat to manually extract
    """
    news_link = forms.CharField(max_length=500)



class SearchForm(forms.Form):
    
    all = forms.BooleanField(widget=forms.CheckboxInput(),initial=False,required=False)
    header = forms.BooleanField(widget=forms.CheckboxInput(), initial=False,required=False)
    body = forms.BooleanField(widget=forms.CheckboxInput(),initial=False,required=False)
    source = forms.BooleanField(widget=forms.CheckboxInput(),initial=False,required=False)
    location = forms.BooleanField(widget=forms.CheckboxInput(),initial=False,required=False)
    death_no = forms.BooleanField(widget=forms.CheckboxInput(),initial=False,required=False)
    injury_no = forms.BooleanField(widget=forms.CheckboxInput(),initial=False,required=False)
    date = forms.BooleanField(widget=forms.CheckboxInput(),initial=False,required=False)
    year = forms.BooleanField(widget=forms.CheckboxInput(),initial=False,required=False)
    month = forms.BooleanField(widget=forms.CheckboxInput(),initial=False,required=False)
    day = forms.BooleanField(widget=forms.CheckboxInput(),initial=False,required=False)

    search_text = forms.CharField(widget=forms.TextInput(attrs={'style':'width:60%'}))
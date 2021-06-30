from django import forms


class NameForm(forms.Form):
    """
    input: news link youu wnat to manually extract
    """
    news_link = forms.CharField(max_length=500)
from boardgamegeek import BGGClient
from django import forms
from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(label="query")

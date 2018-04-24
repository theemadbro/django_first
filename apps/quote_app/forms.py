from django import forms

class quoteForm(forms.Form):
    name = forms.CharField(min_length=3, max_length=55)
    quote = forms.CharField(min_length=15, max_length=455)

from django import forms
import datetime

today = datetime.date.today()

class NameForm(forms.Form):
    name = forms.CharField(min_length=3, max_length=35, widget=forms.TextInput(attrs={'pattern':"[A-Z a-z']+", 'title':'Enter Characters Only'}))
    username = forms.CharField(min_length=3, max_length=22)
    email = forms.CharField(min_length=3, max_length=35, widget=forms.EmailInput())
    password = forms.CharField(min_length=8, max_length=32, widget=forms.PasswordInput())
    passcheck = forms.CharField(min_length=8, max_length=32, widget=forms.PasswordInput())
    birthday = forms.DateField(widget=forms.widgets.DateInput(attrs={'type':'date', 'max':today}))

class LoginForm(forms.Form):
    inuser = forms.CharField(min_length=3, max_length=55)
    inpass = forms.CharField(min_length=8, max_length=32, widget=forms.PasswordInput)
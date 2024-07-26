from django import forms

class SimpleForm(forms.Form):
    videoId = forms.CharField(label='Enter YT video id:', max_length=100)

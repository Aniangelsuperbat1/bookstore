from django import forms

class ReviewForm(forms.Form):
    body = forms.CharField()
    image = forms.ImageField()
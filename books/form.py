from django import forms

class ReviewForm(forms.Form):
    body = forms.TEXTarea()
    image = forms.ImageField()
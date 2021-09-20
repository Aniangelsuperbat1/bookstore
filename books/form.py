from django import forms

class ReviewForm(forms.Form):
    body = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField()
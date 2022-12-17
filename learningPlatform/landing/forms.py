from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    title = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '1',
            'placeholder': 'Choose an interesting title...'
        }))
    body = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Share your work...'
        }))
    class Meta:
        model = Review
        fields = ["title", "body", "rating"]
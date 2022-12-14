from django import forms
from .models import Post, Comment, Supoort_ticket

class PostForm(forms.ModelForm):
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
        model = Post
        fields = ["title", "body", "document"]

class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '1',
            'placeholder': 'Say Something...'
        }))

    class Meta:
        model = Comment
        fields = ["comment", "rating"]
class SupportForm(forms.ModelForm):
    issue = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '1',
            'placeholder': "What is your issue?"
        }))
    description = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Describe in detail'
        }))
    class Meta:
        model = Supoort_ticket
        fields= ["issue", "description"]
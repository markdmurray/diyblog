from django import forms

class CommentForm(forms.Form):

    description = forms.CharField(widget=forms.Textarea, max_length=200)
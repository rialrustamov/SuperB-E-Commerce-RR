from django import forms
from django.forms import fields, widgets

from blog.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (['author','message',])
        widgets = {
            'author': widgets.TextInput(attrs={'class': 'input-text'} ),
            'message': widgets.Textarea(attrs={'class': 'form-control', 'rows': 5, 'cols': 50} ),
        }
from django import forms
from .views import Blog

class Styling:

    title = {
        'placeholder': 'Enter Title',
        'id': 'title',
        'class': 'form-control w-50',
        'autocomplete': 'off'
        }
    
    body = {
        'placeholder': 'What are you feeling today?',
        'id': 'body',
        'class': 'form-contrl w-50',
    }

class BlogCreateForm(forms.ModelForm):

    title = forms.CharField(max_length=60, required=True, widget=forms.TextInput(attrs=Styling.title))
    body = forms.CharField(required=True, widget=forms.Textarea(attrs=Styling.body))

    class Meta:
        model = Blog
        fields = ['title','body']
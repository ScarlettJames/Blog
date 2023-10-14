from django import forms
from .models import Profile

class Styling:

    passwordOne = {
        'placeholder': 'Enter Your Password',
        'id': 'passwordTwo',
        'class': 'form-control w-50',
        'autocomplete': 'off'
        }
    passwordTwo = {
        'placeholder': 'Confirm Your Password',
        'id': 'passwordTwo',
        'class': 'form-control w-50',
        }
    username = {
        'placeholder': 'Enter Your Username',
        'class': 'form-control w-50',
        'autocomplete': 'off'
    }

    email = {
        'placeholder': 'Enter Email',
        'class': 'form-control w-50'
    }

    firstname = {
        'placeholder': 'First Name',
        'class': 'form-control w-50'
    }

    lastname = {
        'placeholder': 'Last Name',
        'class': 'form-control w-50'
    }

class UserForm(forms.Form):

    firstname = forms.CharField(max_length=16,min_length=4,strip=True,required=True, label='Firstname',
                               widget=forms.TextInput(attrs=Styling.firstname))
    lastname = forms.CharField(max_length=16,min_length=4,strip=True,required=True, label='Lastname',
                               widget=forms.TextInput(attrs=Styling.lastname))
    username = forms.CharField(max_length=16,min_length=4,strip=True,required=True, label='Username',
                               widget=forms.TextInput(attrs=Styling.username))
    email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs=Styling.email),required=True)
    passwordOne = forms.CharField(max_length=16,min_length=8,required=True, label='Password',
                               widget=forms.PasswordInput(attrs=Styling.passwordOne))
    passwordTwo = forms.CharField(max_length=16,min_length=8,required=True, label='Confirm Password',
                               widget=forms.PasswordInput(attrs=Styling.passwordTwo))
    
class LoginForm(forms.Form):

    email = forms.EmailField(widget=forms.EmailInput(attrs=Styling.email),required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs=Styling.passwordOne),required=True)

class ProfileForm(forms.ModelForm):
    image = forms.ImageField()

    class Meta:
        model = Profile
        fields = ['image']
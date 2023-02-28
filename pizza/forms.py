from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

from .models import (
    Bookings, NewsLetter, UserProfile,Comment
)

class UserUpdate(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {
            'username' : forms.TextInput(attrs={'class': 'form-input', 'placeholder':'Username'}),
            'email' : forms.EmailInput(attrs={'class': 'form-input', 'placeholder':'Email'}),
            'first_name' : forms.TextInput(attrs={'class': 'form-input', 'placeholder':'First Name'}),
            'last_name' : forms.TextInput(attrs={'class': 'form-input', 'placeholder':'Last Name'})
        }

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone',]
        widgets = {
            'phone' : forms.TextInput(attrs={'class': 'form-input', 'placeholder':'phone'}),
        }


class BookingForm(forms.ModelForm):
    class Meta:
        model = Bookings
        fields = [
            'name',
            'email',
            'service',
            'message'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
            'service': forms.Select(),
            'message': forms.Textarea(attrs={'class': 'form-input textarea-lg'}),
        }


class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-input'}),

        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['subject', 'comment']
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-input'}),
            'comment': forms.Textarea(attrs={'class': 'form-input textarea-lg'}),
        }
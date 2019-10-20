from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# Inherit from UserCreationForm
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    # Class Meta gives nested namespace for configuration
    #   and keeps configuration in one place
    # Effected model is User, e.g. form.save() saves to User model
    # Fields are the fields in the form in this order
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

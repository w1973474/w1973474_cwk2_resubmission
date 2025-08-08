from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(required=True, max_length=30)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'password1', 'password2')


User = get_user_model()

class AddUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'role']


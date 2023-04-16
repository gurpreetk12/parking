from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Search


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
class SearchForm(forms.ModelForm):
    address = forms.CharField(label='')

    class Meta:
        model = Search
        fields = ['address', ]
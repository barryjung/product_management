from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class LoginForm(AuthenticationForm):
    pass
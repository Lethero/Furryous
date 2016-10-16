from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(label="Password", max_length=100, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "password")

    def clean(self):
        return super(LoginForm, self).clean()

class RegisterForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(label="Password", max_length=100, widget=forms.PasswordInput)
    confirm_password = forms.CharField(label="Confirm Password", max_length=100, widget=forms.PasswordInput)
    email = forms.EmailField(label="Email", max_length=256)

    class Meta:
        model = User
        fields = ("username", "password")
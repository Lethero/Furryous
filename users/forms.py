from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100, required=True)
    password = forms.CharField(label="Password", max_length=100, widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = ("username", "password")

    def clean(self):
        return super(LoginForm, self).clean()

class RegisterForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100, required=True)
    username.widget.attrs["required"] = "required"
    password = forms.CharField(label="Password", max_length=100, widget=forms.PasswordInput, required=True)
    password.widget.attrs["required"] = "required"
    confirm_password = forms.CharField(label="Confirm Password", max_length=100, widget=forms.PasswordInput, required=True)
    confirm_password.widget.attrs["required"] = "required"
    email = forms.EmailField(label="Email", max_length=256, required=True)
    email.widget.attrs["required"] = "required"

    class Meta:
        model = User
        fields = ("username", "password")
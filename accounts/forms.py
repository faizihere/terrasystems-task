from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# PUPOSE : TO RENDER THE USER REGISTRATION FORM IN REGISTRATION PAGE
class RegisterForm(UserCreationForm):
    username = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'placeholder': 'Email'})
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def clean_username(self):
        email = self.cleaned_data['username']
        if User.objects.filter(username=email).exists():
            raise forms.ValidationError("Email is already registered.")
        return email


# PUPOSE : TO RENDER THE USER LOGIN FORM IN LOGIN PAGE
class LoginForm(forms.Form):
    username = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={
        'placeholder': 'Enter your email',
        'class': 'form-control'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter your password',
        'class': 'form-control'
    }))


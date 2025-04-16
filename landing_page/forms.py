from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import HomePageContent, PricingPlan


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


# PUPOSE : TO RENDER THE HOME PAGE (CONTENT) FIELDS IN EDIT PAGE OF THE DASHBOARD
class HomePageContentContentForm(forms.ModelForm):
    class Meta:
        model = HomePageContent
        fields = '__all__'

    # PURPOSE : TO LOAD THE STYLES FOR DJANGO BASED FORMS USING TAILWIND CSS
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full sm:w-3/4 px-4 py-3 mt-2 bg-gray-800 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500 text-white shadow-md transition duration-300 ease-in-out hover:border-indigo-500'
    }))
    subtitle = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full sm:w-3/4 px-4 py-3 mt-2 bg-gray-800 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500 text-white shadow-md transition duration-300 ease-in-out hover:border-indigo-500'
    }))
    cta_button = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full sm:w-3/4 px-4 py-3 mt-2 bg-gray-800 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500 text-white shadow-md transition duration-300 ease-in-out hover:border-indigo-500'
    }))

    feature_title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full sm:w-3/4 px-4 py-3 mt-2 bg-gray-800 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500 text-white shadow-md transition duration-300 ease-in-out hover:border-indigo-500'
    }))
    feature_description = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full sm:w-3/4 px-4 py-3 mt-2 bg-gray-800 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500 text-white shadow-md transition duration-300 ease-in-out hover:border-indigo-500'
    }))
    feature_button = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full sm:w-3/4 px-4 py-3 mt-2 bg-gray-800 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500 text-white shadow-md transition duration-300 ease-in-out hover:border-indigo-500'
    }))

    footer_tagline = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full sm:w-3/4 px-4 py-3 mt-2 bg-gray-800 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500 text-white shadow-md transition duration-300 ease-in-out hover:border-indigo-500'
    }))
    contact_email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'w-full sm:w-3/4 px-4 py-3 mt-2 bg-gray-800 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500 text-white shadow-md transition duration-300 ease-in-out hover:border-indigo-500'
    }))
    contact_phone = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full sm:w-3/4 px-4 py-3 mt-2 bg-gray-800 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500 text-white shadow-md transition duration-300 ease-in-out hover:border-indigo-500'
    }))


# PUPOSE : TO RENDER THE PRICING PLAN (CONTENT) FIELDS IN EDIT PAGE OF THE DASHBOARD
class PricingPlanForm(forms.ModelForm):
    class Meta:
        model = PricingPlan
        fields = ['title', 'price', 'features']
        widgets = {
            'features': forms.TextInput(attrs={'rows': 5}),
        }

    # PURPOSE : TO LOAD THE STYLES FOR DJANGO BASED FORMS(EDIT PRICING PLAN) USING TAILWIND CSS
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full sm:w-3/4 px-4 py-3 mt-2 bg-gray-800 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500 text-white shadow-md transition duration-300 ease-in-out hover:border-indigo-500'
    }))

    price = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full sm:w-3/4 px-4 py-3 mt-2 bg-gray-800 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500 text-white shadow-md transition duration-300 ease-in-out hover:border-indigo-500'
    }))

    features = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full sm:w-3/4 px-4 py-3 mt-2 bg-gray-800 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500 text-white shadow-md transition duration-300 ease-in-out hover:border-indigo-500'
    }))

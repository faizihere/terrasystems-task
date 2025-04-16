
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm
from django.shortcuts import render, redirect
from landing_page.models import HomePageContent
from landing_page .models import PricingPlan

# PURPOSE : TO PERFORM USER REGISTRATION AND ITS VALIDATION
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']  # This itself is the email
            password = form.cleaned_data['password1']
            User.objects.create_user(username=username, password=password)
            messages.success(request, "Account created successfully! Please log in.")
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


# PURPOSE : TO PERFORM USER LOGIN AND ITS VALIDATION
def login_view(request):    

    if request.user.is_authenticated:
        return redirect('dashboard') 
    
    if request.method == 'POST':
        form = LoginForm(request.POST)                
        if form.is_valid():            
            username = form.cleaned_data['username'] # This itself is the email
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)                
                return redirect('dashboard')
            else:
                print("error")
                messages.error(request, "Invalid email or password.")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


# PURPOSE : TO PERFORM LOGOUT
def logout_view(request):
    logout(request)
    return redirect('login')

# TO REDIRECT/LOAD THE HOME/LANDING PAGE
def home(request):
    content = HomePageContent.objects.first()
    plans = PricingPlan.objects.all()
    for plan in plans:
        plan.features_list = plan.features.split(',')  # Create a list of features
    return render(request, 'home.html', {'content': content, 'plans':plans})

# TO REDIRECT/LOAD THE CUSTOM ADMIN DASHBOARD
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


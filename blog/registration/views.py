from django.shortcuts import render
from registration import forms, models

# Create your views here.
def index(request):
    return render(request, "index.html")

def registration_view(request):
    registration_form = forms.RegistrationForm
    
    if request.method == "POST":
        registration_form = forms.RegistrationForm(data=request.POST)
        
        if registration_form.is_valid():
            registration_form.save(commit=True)
        else:
            print("Something went wrong.")
            
    registration_dictionary = {'register' : registration_form}
    return render(request, "register.html", context=registration_dictionary)

def login_view(request):
    login_form = forms.LoginForm
    
    if request.method == "POST":
        login_form = forms.LoginForm(data=request.POST)
        
        if login_form.is_valid():
            login_form.save(commit=True)
        else:
            print("Something went wrong.")
            
    login_dictionary = {'login' : login_form}
    return render(request, "login.html", context=login_dictionary)
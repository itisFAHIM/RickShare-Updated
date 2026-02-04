from django.shortcuts import render, redirect

def home_view(request):
    return render(request, 'rides/home.html')

def login_view(request):
    return render(request, 'rides/login.html')

# NEW: The Decision Page
def signup_choice_view(request):
    return render(request, 'rides/signup_choice.html')

# NEW: Passenger Signup
def passenger_signup_view(request):
    return render(request, 'rides/passenger_signup.html')

# NEW: Driver Signup
def driver_signup_view(request):
    return render(request, 'rides/driver_signup.html')
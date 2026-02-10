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

def passenger_dashboard_view(request):
    # Only allow logged-in passengers
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'rides/passenger_dashboard.html')

def request_ride_view(request):
    """Renders the map page for specifying pickup and destination."""
    return render(request, 'rides/request_ride.html')


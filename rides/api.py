from ninja import Router, Schema, Form, File
from ninja.files import UploadedFile
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from .models import Profile, RideRequest
from typing import Optional
from django.contrib.auth import logout
from ninja import Router, Schema
from django.contrib.auth.models import User
from .models import Profile, RideRequest

router = Router()

# --- SCHEMAS ---
class RideSchema(Schema):
    pickup_address: str
    dropoff_address: str
    vehicle_type: str

# --- AUTH ENDPOINTS ---

@router.post("/signup")
def signup(request, 
           username: str = Form(...), 
           email: str = Form(...), 
           password: str = Form(...), 
           phone_number: str = Form(...), 
           user_type: str = Form(...),
           license_number: Optional[str] = Form(None),
           nid_number: Optional[str] = Form(None),
           profile_image: UploadedFile = File(None),
           license_image: UploadedFile = File(None)):
    """
    Handles User & Profile creation with multi-part file uploads.
    """
    # 1. Check if user already exists
    if User.objects.filter(username=username).exists():
        return {"error": "Username already taken. Please try another."}

    # 2. Create the base User
    user = User.objects.create_user(
        username=username,
        email=email,
        password=password
    )
    
    # 3. Create the RickShare Profile with images and license info
    Profile.objects.create(
        user=user,
        phone_number=phone_number,
        user_type=user_type,
        nid_number=nid_number,
        license_number=license_number,
        profile_image=profile_image,
        license_image=license_image,
        is_verified=False  # All accounts start as unverified
    )

    # 4. Log the user in
    login(request, user)
    
    # 5. Conditional Redirection Flow
    if user_type == "DRIVER":
        # Render the "Hold on" page for drivers
        return render(request, 'rides/verification_pending.html')
    
    # Passengers go directly to the dashboard
    return redirect('home')


@router.post("/login")
def login_user(request, 
               identifier: str = Form(...), 
               password: str = Form(...)):
    """
    Allows login via Username OR Phone Number.
    """
    user = authenticate(username=identifier, password=password)
    
    if user is None:
        try:
            profile = Profile.objects.get(phone_number=identifier)
            user = authenticate(username=profile.user.username, password=password)
        except Profile.DoesNotExist:
            pass

    if user is not None:
        login(request, user)
        
        # Check if the user is a driver and if they are verified
        if hasattr(user, 'profile') and user.profile.user_type == "DRIVER":
            if not user.profile.is_verified:
                return render(request, 'rides/verification_pending.html')
        
        return redirect('home')
    
    return {"error": "Invalid phone/username or password"}



class RideSchema(Schema):
    pickup_address: str
    dropoff_address: str
    vehicle_type: str
    # Coordinates sent from the frontend map
    pickup_lat: float
    pickup_lng: float
    dropoff_lat: float
    dropoff_lng: float

@router.post("/request")
def create_ride(request, data: RideSchema):
    if not request.user.is_authenticated:
        return {"error": "Authentication required"}

    ride = RideRequest.objects.create(
        rider=request.user,
        pickup_address=data.pickup_address,
        dropoff_address=data.dropoff_address,
        pickup_lat=data.pickup_lat,
        pickup_lng=data.pickup_lng,
        dropoff_lat=data.dropoff_lat,
        dropoff_lng=data.dropoff_lng,
        vehicle_type=data.vehicle_type,
        status="PENDING"
    )
    return {"id": ride.id, "status": "Request Sent"}





# from ninja import Router, Schema, Form
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.models import User
# from django.shortcuts import redirect
# from .models import Profile, RideRequest
# from ninja import File
# from ninja.files import UploadedFile

# router = Router()

# # --- SCHEMAS (For Mobile App/JSON requests) ---
# class RideSchema(Schema):
#     pickup_address: str
#     dropoff_address: str
#     vehicle_type: str

# # --- AUTH ENDPOINTS ---

# @router.post("/signup")
# def signup(request, 
#            username: str = Form(...), 
#            email: str = Form(...), 
#            password: str = Form(...), 
#            phone_number: str = Form(...), 
#            user_type: str = Form(...)):
        
#     """
#     Handles User & Profile creation. 
#     Uses Form(...) so your HTML <form> can send data directly.
#     """
#     # Check if user already exists
#     if User.objects.filter(username=username).exists():
#         return {"error": "Username already taken. Please try another."}

#     # 1. Create the base User
#     user = User.objects.create_user(
#         username=username,
#         email=email,
#         password=password
#     )
    
#     # 2. Create the RickShare Profile
#     Profile.objects.create(
#         user=user,
#         phone_number=phone_number,
#         user_type=user_type
#     )

#     # 3. Log the user in automatically after signup
#     login(request, user)
    
#     # 4. Redirect to the Home Page (The Uber flow)
#     return redirect('home')


# @router.post("/login")
# def login_user(request, 
#                identifier: str = Form(...), 
#                password: str = Form(...)):
#     """
#     Allows login via Username OR Phone Number.
#     """
#     # 1. Try to authenticate via Username
#     user = authenticate(username=identifier, password=password)
    
#     # 2. If that fails, try via Phone Number
#     if user is None:
#         try:
#             profile = Profile.objects.get(phone_number=identifier)
#             user = authenticate(username=profile.user.username, password=password)
#         except Profile.DoesNotExist:
#             pass

#     if user is not None:
#         login(request, user)
#         return redirect('home')
    
#     return {"error": "Invalid phone/username or password"}


# # --- RIDE ENDPOINTS ---

# @router.post("/request")
# def create_ride(request, data: RideSchema):
#     """
#     Endpoint for a Rider to request a ride.
#     """
#     user = request.user if request.user.is_authenticated else User.objects.first()
    
#     ride = RideRequest.objects.create(
#         rider=user,
#         pickup_address=data.pickup_address,
#         dropoff_address=data.dropoff_address,
#         vehicle_type=data.vehicle_type
#     )
#     return {"id": ride.id, "status": "Looking for drivers nearby..."}



# from django.db import models
# from django.contrib.auth.models import User

# class RideRequest(models.Model):
#     # This links the ride to a user from Django's built-in auth system
#     rider = models.ForeignKey(User, on_delete=models.CASCADE)
#     pickup_address = models.CharField(max_length=255)
#     dropoff_address = models.CharField(max_length=255)
#     vehicle_type = models.CharField(max_length=20) # Bike, CNG, Car
#     status = models.CharField(max_length=20, default="PENDING")

#     def __str__(self):
#         return f"Ride {self.id} - {self.vehicle_type}"
    
from django.db import models
from django.contrib.auth.models import User

# 1. Profile stores the extra info for RickShare users
class Profile(models.Model):
    USER_TYPES = [
        ('RIDER', 'Rider'),
        ('DRIVER', 'Driver'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(max_length=15, unique=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPES)
    profile_image = models.ImageField(upload_to='profiles/', null=True, blank=True)
    nid_number = models.CharField(max_length=20, null=True, blank=True)
    license_number = models.CharField(max_length=50, null=True, blank=True)
    vehicle_type = models.CharField(max_length=10, null=True, blank=True)
    license_image = models.ImageField(upload_to='licenses/', null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    current_lat = models.FloatField(null=True, blank=True)
    current_lng = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} ({self.user_type})"

# 2. RideRequest stores the actual trip data
class RideRequest(models.Model):
    rider = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rides')
    pickup_address = models.CharField(max_length=255)
    dropoff_address = models.CharField(max_length=255)
    
    # New Coordinate Fields
    pickup_lat = models.FloatField(null=True, blank=True)
    pickup_lng = models.FloatField(null=True, blank=True)
    dropoff_lat = models.FloatField(null=True, blank=True)
    dropoff_lng = models.FloatField(null=True, blank=True)
    
    vehicle_type = models.CharField(max_length=20) 
    status = models.CharField(max_length=20, default="PENDING")
    
    # Financial and Logistical Data
    estimated_fare = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    distance_km = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    
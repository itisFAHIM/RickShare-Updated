from django.contrib import admin
from .models import Profile, RideRequest

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'user_type', 'is_verified')
    list_filter = ('user_type', 'is_verified')
    search_fields = ('user__username', 'phone_number', 'nid_number')
    actions = ['approve_drivers']

    def approve_drivers(self, request, queryset):
        queryset.update(is_verified=True)
    approve_drivers.short_description = "Approve selected drivers"

@admin.register(RideRequest)
class RideRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'rider', 'vehicle_type', 'status', 'created_at')
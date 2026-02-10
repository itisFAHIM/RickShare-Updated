# from django.contrib import admin
# from django.urls import path
# from ninja import NinjaAPI
# from rides.api import router as auth_router
# from rides.views import home_view, login_view, signup_view

# api = NinjaAPI()
# api.add_router("/auth/", auth_router)

# urlpatterns = [
#     path('', home_view, name='home'),
#     path('login/', login_view, name='login'),
#     path('signup/', signup_view, name='signup'),
#     path('admin/', admin.site.urls),
#     path('api/', api.urls),
# ]


from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from ninja import NinjaAPI
from rides.api import router as auth_router
# Make sure to import the new view here!
from rides.views import (
    home_view, login_view, signup_choice_view, 
    passenger_signup_view, driver_signup_view,
    passenger_dashboard_view  # Add this import
)

api = NinjaAPI()
api.add_router("/auth/", auth_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('signup/', signup_choice_view, name='signup_choice'),
    path('signup/passenger/', passenger_signup_view, name='passenger_signup'),
    path('signup/driver/', driver_signup_view, name='driver_signup'),
    
    # THIS IS THE MISSING LINE:
    path('passenger/dashboard/', passenger_dashboard_view, name='passenger_dashboard'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# # from django.contrib import admin
# # from django.urls import path
# # from ninja import NinjaAPI
# # from rides.api import router as auth_router
# # from rides.views import home_view, login_view, signup_view

# # api = NinjaAPI()
# # api.add_router("/auth/", auth_router)

# # urlpatterns = [
# #     path('', home_view, name='home'),
# #     path('login/', login_view, name='login'),
# #     path('signup/', signup_view, name='signup'),
# #     path('admin/', admin.site.urls),
# #     path('api/', api.urls),
# # ]


# from django.contrib import admin
# from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import static
# from ninja import NinjaAPI
# from rides.api import router as auth_router
# from . import views

# from rides.views import (
#     home_view, login_view, signup_choice_view, 
#     passenger_signup_view, driver_signup_view,
#     passenger_dashboard_view  
# )

# api = NinjaAPI()
# api.add_router("/auth/", auth_router)

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', api.urls),
#     path('', home_view, name='home'),
#     path('login/', login_view, name='login'),
#     path('signup/', signup_choice_view, name='signup_choice'),
#     path('signup/passenger/', passenger_signup_view, name='passenger_signup'),
#     path('signup/driver/', driver_signup_view, name='driver_signup'),
#     path('request-ride/', views.request_ride_view, name='request_ride'),

#     path('passenger/dashboard/', passenger_dashboard_view, name='passenger_dashboard'),
# ]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from ninja import NinjaAPI
from rides.api import router as auth_router
from rides.views import (
    home_view, login_view, signup_choice_view, 
    passenger_signup_view, driver_signup_view, request_ride_view
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
    # New path for the map-based request page
    path('request-ride/', request_ride_view, name='request_ride'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
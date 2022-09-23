from django.urls import path

from .views import (
    signup,
    dashboard,
    edit_profile,
)

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('dashboard/', dashboard, name='dashboard'),
    path('edit/', edit_profile, name='edit_profile'),
]
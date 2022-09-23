from django.urls import path

from . import views

app_name = 'images'

urlpatterns = [
    path('new/', views.image_create, name='create'),
    path('<slug:slug>/', views.image_detail, name='detail'),
]
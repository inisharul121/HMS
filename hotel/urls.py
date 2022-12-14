"""HMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from hotel import views

urlpatterns = [
    path('', views.home, name='home'),
    path('rooms/', views.room, name='rooms'),
    path('room/<int:pk>/', views.single_room, name='single_room'),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name="logout"),
    #path("booking/<str:pk>/", views.createBooking, name="booking"),
    path("booking/", views.CreateBooking.as_view(), name="booking"),
    path('profile/', views.Profile, name='profile'),
    path('admindashboard/', views.AdminDashboard, name='admindashboard'),
]

from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('login/',loginUser,name='login'),
    path('logout/',logoutUser,name='logout'),
    path('register/',registerUser,name='register'),
    path('apply/',applyPage,name='apply'),
]
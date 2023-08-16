from django.urls import path
from rest_framework import routers

from .views import UserListView,UserSignupView

app_name = 'accounts'

urlpatterns = [
    path('list/',UserListView.as_view()),
    path('sign-up/',UserSignupView.as_view()),
] 


from django.urls import path
from rest_framework import routers

from .views import UserListView,UserSignupView

app_name = 'accounts'

urlpatterns = [
    path('list/',UserListView.as_view()),
    path('sign-up/',UserSignupView.as_view()),
] 



from accounts.views import RegisterView, LoginView, ProfileView

urlpatterns = [
    path('signup/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('profile/<int:pk>', ProfileView.as_view()),
]

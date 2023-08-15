from django.urls import path

from accounts.views import RegisterView, LoginView, ProfileView

urlpatterns = [
    path('signup/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('profile/<int:pk>', ProfileView.as_view()),
]
from django.urls import path,include
from rest_framework import routers

from .views import UserListView,UserSignupView,TakenMediViewSet

app_name = 'accounts'

router = routers.SimpleRouter()
router.register(r'taken-medi',TakenMediViewSet)


urlpatterns = [
    path('',include(router.urls)),
    path('list/',UserListView.as_view()),
    path('sign-up/',UserSignupView.as_view()),
] 



from accounts.views import RegisterView, LoginView, ProfileView

urlpatterns = [
    path('signup/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('profile/<int:pk>', ProfileView.as_view()),
]

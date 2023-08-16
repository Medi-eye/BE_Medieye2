"""
URL configuration for confing project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include

from .views import MediViewSet,ScrapListView,ScrapCreateView,ScrapViewSet,ScrapRetrieveView

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'', MediViewSet)
router.register(r'Scrap',ScrapViewSet)


app_name = 'posts'

urlpatterns = [
    path('',include(router.urls)),
    path('<int:pk>/scrap-create/',ScrapCreateView.as_view()),
    path('scrap/<int:pk>/',ScrapRetrieveView.as_view()),
    path('scrap/',ScrapListView.as_view()),
]

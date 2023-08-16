from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated,AllowAny

from .serializers import (UserModelSerializer,UserSignupSerializer,)
from .models import User

# Create your views here.

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    

class UserSignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignupSerializer


class UserSigninView():
    pass

from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response

from accounts.models import Profile
from accounts.serializers import RegisterSerializer, LoginSerializer, ProfileSerializer


# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data
        return Response({"token": token.key}, status=status.HTTP_200_OK)


class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

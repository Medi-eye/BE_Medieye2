from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated,AllowAny

from .serializers import (UserModelSerializer,UserSignupSerializer,UserTakenMediSerializer)
from .models import User, UserTakenMedi

# Create your views here.

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    

class UserSignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignupSerializer


class UserSigninView():
    pass



# 유저의 복용약물을 추가, 리스트, 삭제, 수정할 수 있는 뷰셋
class TakenMediViewSet(ModelViewSet):
    queryset = UserTakenMedi.objects.all()
    serializer_class = UserTakenMediSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return super(TakenMediViewSet, self).get_queryset().filter(user = self.request.user)

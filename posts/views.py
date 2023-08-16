from django.shortcuts import render


from rest_framework.viewsets import generics,ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.shortcuts import get_object_or_404

# Create your views here.


from .serializers import MedicineSerializer,ScrapSerializer,MediScrapListSerializer
from .models import Medicine,Scrap


class MediViewSet(ModelViewSet):
    serializer_class = MedicineSerializer
    queryset = Medicine.objects.all()

# 유저가 즐겨찾기한 약물들을 받아오는 리스트 뷰
    
class ScrapViewSet(ModelViewSet):
    serializer_class = MediScrapListSerializer
    queryset = Scrap.objects.all()

class ScrapListView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        user  = request.user
        data = {}
        for scrap in user.scrap.all():
            medi = Medicine.objects.get(id=scrap.medicine.id)
            data += MedicineSerializer(instance=medi).data
        return Response(data=data,status=status.HTTP_200_OK)

# 약물 즐겨찾기를 추가하는 시리얼라이저
class ScrapCreateView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, pk, *args, **kwargs):

        scrap = Scrap.objects.create(
            user = request.user,
            medicine = get_object_or_404(Medicine, id = pk),
        )
        scrap.save()
        serializer = ScrapSerializer(scrap)
        return Response(serializer.data,status=status.HTTP_201_CREATED)


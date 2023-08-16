from rest_framework.serializers import ModelSerializer,SerializerMethodField

from rest_framework.response import Response
from rest_framework import status

from .models import Medicine,Scrap


class MedicineSerializer(ModelSerializer):

    class Meta:
        model = Medicine
        fields = '__all__'

    

class ScrapSerializer(ModelSerializer):
    
    class Meta:
        model = Scrap
        fields = '__all__'

# 즐겨찾기 약물 리스트 시리얼라이저
# class MediScrapSerializer(ScrapSerializer):

#     class Meta(ScrapSerializer.Meta):
#         object = Scrap
#         fields = [
#             'medicine', 'user',
#         ]
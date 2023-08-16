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
        fields = [
            'user','medi_id','medi_name'
        ]

    def create(self, validated_data):
        id = validated_data['medi_id']
        scrap = Scrap.objects.create(
            user = self.context['request'].user,
            medi_id = id,
            medi_name = Medicine.objects.get(id=id).name
        )
        return scrap
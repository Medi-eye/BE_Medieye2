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

    def create(self, validated_data):
        scrap = Scrap.objects.create(**validated_data)
        scrap.user = self.context['request'].user
        scrap.save()
        return scrap
    

class MediScrapListSerializer(ScrapSerializer):
    posts = SerializerMethodField()

# obj = scrap(self.request.user)
    def get_medicines(self, obj):
        return MedicineSerializer(obj,many=True).data

    class Meta(ScrapSerializer.Meta):
        fields = ['posts']
from rest_framework.serializers import ModelSerializer,EmailField,CharField,ValidationError,SerializerMethodField
from rest_framework.validators import UniqueValidator

from django.contrib.auth.password_validation import validate_password

from .models import User,Disease,Allergy,UserTakenMedi
from posts.serializers import MedicineSerializer,Medicine


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserSignupSerializer(ModelSerializer):
    email = EmailField(
        required = True,
        validators = [UniqueValidator(queryset=User.objects.all())]
    )

    password = CharField(write_only=True, required=True, validators=[validate_password])
    password2 = CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'password2', 'email', 'phone','age','pregnancy']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise ValidationError({"password": "Password fields didn't match."})
        return attrs
    
    def create(self, validated_data):
        del validated_data['password2']
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class UserTakenMediSerializer(ModelSerializer):

    class Meta:
        model = UserTakenMedi
        fields = '__all__'
        
    def create(self, validated_data):
        id = validated_data['medi_id']
        takenMedi = UserTakenMedi.objects.create(
            user = self.context['request'].user,
            medi_id = id,
            medi_name = Medicine.objects.get(id=id).name
        )
        return takenMedi


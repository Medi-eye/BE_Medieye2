from rest_framework.serializers import ModelSerializer,EmailField,CharField,ValidationError,SerializerMethodField
from rest_framework.validators import UniqueValidator

from django.contrib.auth.password_validation import validate_password

from .models import User,Disease,Allergy


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
    



# class MedicineSerializer(ModelSerializer):
#     class Meta:
#         model = medicine
#         fields ='__all__'

#     def create(self, validated_data):
#         medi = medicine.objects.create(**validated_data)
#         medi.user = self.context['request'].user
#         medi.save()
#         return medi



# class DiseaseMediSerializer(ModelSerializer):
#     medicines = SerializerMethodField()

#     def get_medicines(self,obj):
#         medi = obj.disease_medi.all()
#         return MedicineSerializer(instance=medi, many=True).data['name']

#     class Meta:
#         model = disease
#         fields = [
#             'name', 'medicines'
#             ]
        
# class AllergyMediSerializer(ModelSerializer):
#     medicines = SerializerMethodField()

#     def get_medicines(self,obj):
#         medi = obj.allergy_medi.all()
#         return MedicineSerializer(instance=medi,many=True).data['name']
    
#     class Meta:
#         model = allergy 
#         fields = [
#             'name', 'medicines'
#         ]

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework.authtoken.models import Token

from accounts.models import Profile


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email')

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user:
            token = Token.objects.get(user=user)
            return token
        raise serializers.ValidationError(
            {"error": "Unable to log in with provided credentials."}
        )

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("nickname", "birth", "phone_number", "image")

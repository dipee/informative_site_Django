from rest_framework import serializers
from rest_framework import viewsets
from .models import HeaderImage, Testimonial, Services, ContactUs
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        user = User(
        email=validated_data['email'],
        username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user

class HeaderImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeaderImage
        fields = '__all__'

class ServicesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Services
        fields = '__all__'
    
class TestimonailSerializer( serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'
    
class ContactSerializer(serializers.ModelSerializer):
    class Meta: 
        model = ContactUs
        fields = '__all__'
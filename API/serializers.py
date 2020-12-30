from rest_framework import serializers
from rest_framework import viewsets
from .models import HeaderImage, Testimonial, Services, ContactUs
from rest_framework.authtoken.models import Token





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
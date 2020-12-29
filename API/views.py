
from .models import HeaderImage, Services, Testimonial, ContactUs, TestModel 
from .serializers import HeaderImageSerializer, ServicesSerializer, TestimonailSerializer, UserSerializer, ContactSerializer

#from rest framework
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets,status, generics
from rest_framework import permissions

# for front end 
from django.shortcuts import render
# Create your views here.

def index(request):
    header = HeaderImage.objects.all()
    return render(request, "index.html",{
        "headers":header
    }
    )


class TestView(APIView):
    def get(self, request):
        last_object =  TestModel.objects.last() 
        if not last_object:
            return Response({"message":"no objects present"})
        else:
            max_id = last_object.pk
            max_id_unique = "up-"+"{0:0=3d}".format(max_id)
            return Response({"message":max_id_unique})


class HeaderImageViewSet(viewsets.ModelViewSet):
    queryset = HeaderImage.objects.all()
    serializer_class = HeaderImageSerializer
    

class ServicesViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    
class TestimonailViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonailSerializer

class ContactViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = ContactUs.objects.all()
    serializer_class = ContactSerializer
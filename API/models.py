from django.db import models

# Create your models here.
class HeaderImage(models.Model):
    title = models.CharField(max_length=200)
    is_active = models.BooleanField()
    image = models.ImageField(upload_to='Mainslider', null=True, default=None)
    header_url = models.URLField(max_length=200, null=True, default=None)

    def __str__(self):
        return self.title

class Services(models.Model):

    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='services', null=True, default = None)
    description = models.TextField()
    services_url = models.URLField(max_length=200, null=True, default=None)

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    clientName = models.CharField(max_length=100)
    review = models.TextField()
    logo = models.ImageField(upload_to = 'testimonial', null = True, default = None)

    def __str__(self):
        return self.clientName

class ContactUs(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
        return self.firstName


class TestModel(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
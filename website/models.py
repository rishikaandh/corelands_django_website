from django.db import models

# Create your models here.
class Propertie(models.Model):
    PROPERTY_TYPE_CHOICES = [
        ('commercial', 'Commercial'),
        ('house', 'House'),
        ('land', 'Land'),
    ]

    FACING_CHOICES = [
        ('east', 'East'),
        ('west', 'West'),
        ('north', 'North'),
        ('south', 'South'),
    ]

    CLASS_CHOICES = [
        ('residential', 'Residential Area'),
        ('agriculture', 'Agriculture Land'),
    ]

    SALE_TYPE_CHOICES = [
        ('sale', 'Sale'),
        ('lease', 'Lease'),
        ('rent', 'Rent'),
    ]

    property_id = models.AutoField
    location = models.CharField(max_length=255)
    price = models.IntegerField()
    property_type = models.CharField(max_length=20,choices=PROPERTY_TYPE_CHOICES)
    facing = models.CharField(max_length=10, choices=FACING_CHOICES)
    landmark = models.CharField(max_length=255)
    land_area = models.CharField(max_length=100)
    size_and_frontage = models.CharField(max_length=100)
    property_class = models.CharField(max_length=20, choices=CLASS_CHOICES)
    number_of_owners = models.IntegerField()
    sale_type = models.CharField(max_length=10, choices=SALE_TYPE_CHOICES)
    image1 = models.ImageField(upload_to='images/', null=True, blank=True)
    image2 = models.ImageField(upload_to='images/', null=True, blank=True)
    image3 = models.ImageField(upload_to='images/', null=True, blank=True)
    image4 = models.ImageField(upload_to='images/', null=True, blank=True)
    image5 = models.ImageField(upload_to='images/', null=True, blank=True)

    video1 = models.FileField(upload_to='videos/', null=True, blank=True)
    video2 = models.FileField(upload_to='videos/', null=True, blank=True)
    video3 = models.FileField(upload_to='videos/', null=True, blank=True)


    def __str__(self):
        return f"{self.location} - {self.property_type} - Rs.{self.price}"

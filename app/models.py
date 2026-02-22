from django.db import models
from django.contrib.auth.models import User
# Create your models here.
    
class fert_Details(models.Model):
    farmer_name = models.CharField(max_length=100)
    n = models.PositiveIntegerField()
    p = models.PositiveIntegerField()
    k = models.PositiveIntegerField()
    temperature = models.CharField(max_length=20)
    humidity = models.CharField(max_length=20)
    prediction = models.CharField(max_length=50)
    fertilizer = models.CharField(max_length=50)
    date = models.DateField()

    def __str__(self):
        return self.farmer_name
    
class images_data(models.Model):
      Images = models.FileField(upload_to='Images')    

class image_data(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    Images = models.FileField(upload_to='crop_images/')
    quantity = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.Images.name} - {self.quantity} Kg"


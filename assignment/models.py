from django.db import models

# Create your models here.
class Detailsofuser(models.Model):
      
    username = models.CharField(max_length=100)  
    email= models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    
    class Meta:
        pass

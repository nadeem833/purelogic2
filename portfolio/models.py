from django.db import models

# Create your models here.
class Contact (models.Model):
    name=models.name = models.CharField(max_length=25) 
    email=models.EmailField(max_length=25)
    phonenumber=models.CharField( max_length=12)
    decrption=models.TextField()

    def __str__(self):
        return self.name


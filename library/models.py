from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class ExampleModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
       
class OsfaDepartment(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    code = models.CharField(max_length=5, blank=False, null=False)
    description = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
class OsfaUser(AbstractUser):
    extra_field = models.CharField(max_length=100, blank=True)
    department = models.ForeignKey(OsfaDepartment, on_delete=models.CASCADE, null=True, blank=True, related_name="users")  
     
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
    
    
class OsfaRequestUser(models.Model):
    user = models.ForeignKey("OsfaUser", on_delete=models.CASCADE)
    request = models.ForeignKey("OsfaRequests", on_delete=models.CASCADE)
    request_signed = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        unique_together = ('user', 'request')

class OsfaUser(AbstractUser):
    extra_field = models.CharField(max_length=100, blank=True)
    department = models.ForeignKey(OsfaDepartment, on_delete=models.CASCADE, null=True, blank=True, related_name="users", verbose_name='Department')  
    isRequestor = models.BooleanField(null=False, default=False, verbose_name='Is Requestor')
    isRequestorAdmin = models.BooleanField(null=False, default=False, verbose_name='Is Requestor Admin')
    isRequestorProgrammer = models.BooleanField(null=False, default=False, verbose_name='Is Requestor Programmer')
     
class OsfaRequests(models.Model):
    number = models.IntegerField(unique=True, null=False)
    request_date = models.DateField(null=False)
    subject = models.CharField(max_length=256, null=False)
    status = models.CharField(max_length=32, null=True)
    priority = models.CharField(max_length=32, null=True)
    source = models.CharField(max_length=32, null=True)
    program = models.CharField(max_length=128, null=True)
    department = models.CharField(max_length=32, null=True)
    deadline = models.CharField(max_length=32, null=True)
    comment = models.TextField(null=True)
    complete_date = models.DateField(null=True)
    delete_date = models.DateTimeField(null=True)
    approved = models.BooleanField(default=False)
    
    users = models.ManyToManyField(
        OsfaUser,
        through='OsfaRequestUser',
        related_name='requests'
    )

    
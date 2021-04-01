from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class StudentUser(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=12,null=True)
    image = models.FileField(null=True)
    gender =models.CharField(max_length=15,null=True)
    type = models.CharField(max_length=15,null=True)

    def __str__(self):
        return self.user.username




class Recruiter(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=12,null=True)
    image = models.FileField(null=True)
    gender =models.CharField(max_length=15,null=True)
    company = models.CharField(max_length=100,null=True)
    type = models.CharField(max_length=15,null=True)
    status = models.CharField(max_length=20,null=True)
    def __str__(self):
        return self.user.username

class Job(models.Model):
    recruiter = models.ForeignKey(Recruiter,on_delete=models.CASCADE)
    satart_date = models.DateField()
    end_date=models.DateField()
    title = models.CharField(max_length=20)
    salary=models.CharField(max_length=20)
    image=models.FileField()
    discription=models.CharField(max_length=100)
    experience=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    skills=models.CharField(max_length=100)
    post_date = models.DateField()

    def __str__(self):
        return self.title
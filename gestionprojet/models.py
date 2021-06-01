from django.db import models
from datetime import datetime
# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=50)
    descr = models.TextField(blank = True)
    date = models.DateTimeField(default=datetime.now())
    cmplte = models.BooleanField(default=False)

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    descrp = models.TextField(blank = True)
    date = models.DateTimeField(default=datetime.now())
    tasks = models.ManyToManyField(Task,null = True,blank=True)

class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    date = models.DateTimeField(default=datetime.now())
    project = models.ManyToManyField(Project,null = True,blank=True)
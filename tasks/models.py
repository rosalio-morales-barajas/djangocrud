from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

# Create your models here.

class Tasks(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    dateCompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)     
    
    def __str__(self):
        return self.title + ' by ' + self.user.username
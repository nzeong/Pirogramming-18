from django.db import models
from turtle import title

# Create your models here.
class Idea(models.Model):
    DEVTOOL_CHOICE = [
        ('django', 'django'),
        ('react', 'react'),
        ('Spring', 'Spring'),
        ('Node.js', 'Node.js'),
        ('Java', 'Java'),
        ('C++', 'C++'),
    ]
    
    title = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='idea', null=True)
    content = models.TextField(null=True)
    interest = models.IntegerField(null=True)
    devtool = models.CharField(max_length=10, choices=DEVTOOL_CHOICE, null=True)
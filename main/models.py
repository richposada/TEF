from django.db import models
from django.contrib import admin

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=150)
	body = models.TextField()
	timestamp = models.DateTimeField()
	
admin.site.register(Post)

class RegisteredPerson(models.Model):
	firstName = models.CharField(max_length=100)
	lastName = models.CharField(max_length=100)
	emailAddress = models.CharField(max_length=100)
	dateCreated = models.DateTimeField()
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=50)
	isActive = models.BooleanField()
	
admin.site.register(RegisteredPerson)
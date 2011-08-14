from django.db import models
from django.contrib import admin
from django.forms import ModelForm
from django import forms
from datetime import datetime


STATES = (
	('AL', 'Alabama'),
	("AL", 'Alabama'),
	("AK", 'Alaska'),
	("AZ", 'Arizona'),
	("AR", 'Arkansas'),
	("CA", 'California'),
	("CO", 'Colorado'),
	("CT", 'Connecticut'),
	("DE", 'Delaware'),
	("FL", 'Florida'),
	("GA", 'Georgia'),
	("HI", 'Hawaii'),
	("ID", 'Idaho'),
	("IL", 'Illinois'),
	("IN", 'Indiana'),
	("IA", 'Iowa'),
	("KS", 'Kansas'),
	("KY", 'Kentucky'),
	("LA", 'Louisiana'),
	("ME", 'Maine'),
	("MD", 'Maryland'),
	("MA", 'Massachusetts'),
	("MI", 'Michigan'),
	("MN", 'Minnesota'),
	("MS", 'Mississippi'),
	("MO", 'Missouri'),
	("MT", 'Montana'),
	("NE", 'Nebraska'),
	("NV", 'Nevada'),
	("NH", 'New Hampshire'),
	("NJ", 'New Jersey'),
	("NM", 'New Mexico'),
	("NY", 'New York'),
	("NC", 'North Carolina'),
	("ND", 'North Dakota'),
	("OH", 'Ohio'),
	("OK", 'Oklahoma'),
	("OR", 'Oregon'),
	("PA", 'Pennsylvania'),
	("RI", 'Rhode Island'),
	("SC", 'South Carolina'),
	("SD", 'South Dakota'),
	("TN", 'Tennessee'),
	("TX", 'Texas'),
	("UT", 'Utah'),
	("VT", 'Vermont'),
	("VA", 'Virginia'),
	("WA", 'Washington'),
	("DC", 'Washington D.C.'),
	("WV", 'West Virginia'),
	("WI", 'Wisconsin'),
	("WY", 'Wyoming'),
)

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=150)
	body = models.TextField()
	timestamp = models.DateTimeField()
	
admin.site.register(Post)

class Friend(models.Model):
	firstName = models.CharField(max_length=200)
	lastName = models.CharField(max_length=200)
	emailAddress = models.EmailField(max_length=75)
	city = models.CharField(max_length=200, blank=True)
	state = models.CharField(max_length=2, choices=STATES, blank=True)
	createdDate = models.DateField(auto_now_add=True)

	
admin.site.register(Friend)

class FriendForm(ModelForm):
	firstName = forms.CharField(error_messages={'required': 'Please provide your first name.'})
	lastName = forms.CharField(error_messages={'required': 'Please provide your last name.'})
	emailAddress = forms.CharField(error_messages={'required': 'Please provide a valid email address.'})
	class Meta:
		model = Friend
		
class ContactForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea(attrs={'rows':20, 'cols':50}), error_messages={'required': 'Please enter your message before submitting.'})
    sender = forms.EmailField(error_messages={'required': 'Please provide a valid email address.'})
    
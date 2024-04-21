from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	profile_pic = models.ImageField(default='default.png', null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name

class ContactMessage(models.Model):
	name = models.CharField(max_length=200, null=False)
	email = models.CharField(max_length=200, null=False)
	subject = models.CharField(max_length=200, null=False)
	message = models.TextField(null=False)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	phone = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.subject
	
	def get_absolute_url(self):
		return reverse('message_detail', args=[str(self.id)])

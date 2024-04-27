from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

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

class Pet(models.Model):
	picture = models.ImageField(upload_to='pets/', default='default.png')
	name = models.CharField(max_length=200)
	age = models.IntegerField()
	animal_type = models.CharField(max_length=200)
	description = models.TextField()
	adopted = models.BooleanField(default=False)
	up_for_adoption = models.BooleanField(default=False)
	adoption_history = models.TextField(default='Never Adopted')
	medical_history = models.TextField(default='No Medical History')
	treatment_history = models.TextField(default='No Treatment History')
	treatment_in_progress = models.BooleanField(default=False)
	treatment_costs = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
	deceased = models.BooleanField(default=False)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name
	
	def get_absolute_url(self):
		return reverse('pet_detail', args=[str(self.id)])
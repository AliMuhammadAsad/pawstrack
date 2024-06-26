from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from .models import * 

class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'
		exclude = ['user']

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User 
		fields = ['username', 'email', 'password1', 'password2']

class ContactForm(ModelForm):
	class Meta:
		model = ContactMessage
		fields = ['name', 'email', 'subject', 'message', 'phone']
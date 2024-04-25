from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from django.views.generic import *
from django.urls import reverse_lazy

# Create your views here.
from .models import *
from .forms import *
from .decorators import unauthenticated_user, allowed_users, admin_only

@unauthenticated_user
def registerPage(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			
			messages.success(request, 'Account was created for '+ username)
			return redirect('login')

	context = {'form': form}

	return render(request, 'accounts/register.html', context)

@unauthenticated_user
def loginPage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username or Password is incorrect!')

	context = {}
	return render(request, 'accounts/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
@admin_only
def home(request):
	return render(request, 'accounts/user.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def userPage(request):
	return render(request, 'accounts/user.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def accountSettings(request):
	customer = request.user.customer
	form = CustomerForm(instance=customer)

	if request.method == 'POST':
		form = CustomerForm(request.POST, request.FILES, instance=customer)
		if form.is_valid():
			form.save()
			
	context = {'form': form} 
	return render(request, 'accounts/account_settings.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'customer'])
def aboutUs(request):
	return render(request, 'accounts/about.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'customer'])
def contactUs(request):
	form = ContactForm()
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Your message has been sent successfully!')
			return redirect('contact')
	context = {'form': form}
	return render(request, 'accounts/contact.html', context)

@login_required(login_url='login')
@admin_only
def viewMessages(request):
	messages = ContactMessage.objects.all()
	context = {'messages': messages}
	return render(request, 'accounts/messages.html', context)

class MessageDetailView(DetailView):
	model = ContactMessage

class MessageDeleteView(DeleteView):
	model = ContactMessage
	success_url = reverse_lazy('messages')

class PetListView(ListView):
	model = Pet

class PetDetailView(DetailView):
	model = Pet

class PetCreateView(CreateView):
	model = Pet
	fields = '__all__'

	def get_success_url(self):
		return reverse_lazy('pet_list')

class PetUpdateView(UpdateView):
	model = Pet
	fields = '__all__'

	def get_success_url(self):
		return reverse_lazy('pet_list')

class PetDeleteView(DeleteView):
	model = Pet
	success_url = '/pets/'
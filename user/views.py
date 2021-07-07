from django import views
from django.contrib.auth import authenticate
import user
from django.shortcuts import render
from .forms import *
from django.shortcuts import redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from trip.models import Station

# --------------------------REGISTRATION--------------------------------
class UserRegistration(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            form = UserRegistrationForm()
            context = {'form': form}
            request.title = "User Registration"
            return render(request, 'user/registration.html', context)

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('login')
        else:
            form = UserRegistrationForm(data=request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')

            context = {'form': form}
            return render(request, 'user/registration.html', context)


# ----------------------------------USERLOGIN-------------------------------------

def userLogin(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST['username']
            passw = request.POST['password']

            user =  authenticate(request, username=username, password=passw)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return HttpResponse('your password is wrong')

        return render(request, 'user/login.html')

# --------------------------------USERLOGOUT-------------------------------
def userLogout(request):
    logout(request)
    return redirect('login')


# ------------------------DRIVER REGISTRATION------------------------------

class DriverRegistration(View):
    def get(self, request):
        form = DriverForm()
        userForm = UserRegistrationForm()
        context = {'form': form, 'userForm': userForm}
        request.title = "Driver Registration"
        return render(request, 'user/driver/driver_registration.html', context)
    def post(self, request):
        form = DriverForm(data=request.POST)
        userForm = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            dForm = form.save(commit=False)
            dForm.user = request.user
            dForm.save()
            
            form.save()
            return redirect('/')



        context = {'form': form, 'userForm': userForm}
        return render(request, 'user/driver/driver_registration.html', context)


# -----------------------------------BUS-----------------------------------------

class BusRegistration(View):
    def get(self, request):
        try:
            driver = request.user.driver
        except:
            driver = False
        if driver:
            busform = BusForm()
            context = {'busform': busform}
            request.title = "Buses Registration"
            return render(request, 'user/driver/bus_registration.html', context)
        else:
            return redirect("userprofile")
    def post(self, request):
        
        busform = BusForm(data=request.POST)
        
        if busform.is_valid():
            bForm = busform.save(commit=False)
            bForm.driver = request.user.driver
            bForm.save()
            print(bForm)
            # busform.save()
            return redirect('userprofile')

        context = {'busform': busform}
        return render(request, 'user/driver/bus_registration.html', context)


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'user/about.html')

def blog(request):
    return render(request, 'user/blog.html')

def contact(request):
    return render(request, 'user/contact.html')

def portfolio(request):
    return render(request, 'user/portfolio.html')

def team(request):
    return render(request, 'user/team.html')



def profile(request):
    
    return render(request, 'profile.html')




from django.forms.models import ModelForm
from user.validators import PhoneValidator
from django.forms import fields, widgets
from django.forms.forms import Form
from .models import *
from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError




class UserForm(UserCreationForm):
    # username = forms.CharField(max_length=100, required=True)
    # first_name = forms.CharField(max_length=100, required=True)
    # last_name = forms.CharField(max_length=100, required=True)
    # phone = forms.CharField(max_length=114, validators=[PhoneValidator()], required=True)
    # password1 = forms.CharField(max_length=100, widget=forms.PasswordInput, validators=[MinLengthValidator(8)], required=True)
    # password2 = forms.CharField(max_length=100, widget=forms.PasswordInput, validators=[MinLengthValidator(8)], required=True)
    
    
    def clean_phone(self):
        if User.objects.filter(phone=self.cleaned_data.get('phone')).exists():
            raise ValidationError('Phone number is already exists')
        return self.cleaned_data['phone']
    


    class Meta:
        model = User
        fields = ['username', 'first_name','last_name','phone', 'password1','password2']



class UserRegistrationForm(UserCreationForm):
    # username = forms.CharField(max_length=100, required=True)
    # first_name = forms.CharField(max_length=100, required=True)
    # last_name = forms.CharField(max_length=100, required=True)
    phone = forms.CharField(max_length=114, validators=[PhoneValidator()], required=True)
    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput, validators=[MinLengthValidator(8)], required=True)
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput, validators=[MinLengthValidator(8)], required=True)




    # def clean_username(self):
    #     if User.objects.filter(username=self.cleaned_data.get('username')).exists():
    #         raise ValidationError('Username is already exists')
    #     return self.cleaned_data['username']

    # def clean_phone(self):
    #     if User.objects.filter(phone=self.cleaned_data.get('phone')).exists():
    #         raise ValidationError('Phone number is already exists')
    #     return self.cleaned_data['phone']

    # def clean_confirm(self):
    #     if self.cleaned_data['password1'] != self.cleaned_data['password2']:
    #         raise ValidationError('Passwords should be the same...')
    #     return self.cleaned_data['password2']

    class Meta:
        model = User
        fields = ['username', 'first_name','last_name','phone', 'password1','password1']
        widgets = {
            'username': forms.TextInput(attrs={"type":"text", "class": "form-control", "id": "name", "placeholder": "Your Name", "required": "required", "data-validation-required-message": "Please enter your name"}),
            'first_name': forms.TextInput(attrs={"type":"text", "class": "form-control", "id": "name", "placeholder": "Your Fist Name", "required": "required", "data-validation-required-message": "Please enter your name"}),
            'last_name': forms.TextInput(attrs={"type":"text", "class": "form-control", "id": "name", "placeholder": "Your Last Name", "required": "required", "data-validation-required-message": "Please enter your name"}),
            'phone': forms.TextInput(attrs={"type":"text", "class": "form-control", "id": "name", "placeholder": "Your Phone Number", "required": "required", "data-validation-required-message": "Please enter your name"}),
            'password1': forms.TextInput(attrs={"type":"text", "class": "form-control", "id": "name", "placeholder": "Your Password", "required": "required", "data-validation-required-message": "Please enter your name"}),
            'password2': forms.TextInput(attrs={"type":"text", "class": "form-control", "id": "name", "placeholder": "Password Confirm", "required": "required", "data-validation-required-message": "Please enter your name"}),
        }

class DriverForm(ModelForm):
    class Meta:
        model = Driver
        fields = "__all__"
        exclude =['user']
        # widgets = {
        #     'image': forms.FileInput(attrs={ "class": "form-control", "id": "name", "placeholder": "Your Name", "required": "required", "data-validation-required-message": "Please enter your name"}),
        #     'birthday': forms.DateInput(attrs={ "class": "form-control", "id": "email", "placeholder": "Your Birthday", "required": "required", "data-validation-required-message": "Please enter your name"}),
        #     'gender': forms.TextInput(attrs={ "class": "form-control", "id": "name", "placeholder": "Your Name", "required": "required", "data-validation-required-message": "Please enter your name"}),
        #     'smoking': forms.CheckboxInput(attrs={ "class": "form-control", "id": "name", "placeholder": "Your Name", "required": "required", "data-validation-required-message": "Please enter your name"}),
        #     'experience': forms.NumberInput(attrs={ "class": "form-control", "id": "name", "placeholder": "Your Name", "required": "required", "data-validation-required-message": "Please enter your name"}),
        # }

class BusForm(ModelForm):
    class Meta:
        model = Bus
        fields = "__all__"
        exclude =['driver']
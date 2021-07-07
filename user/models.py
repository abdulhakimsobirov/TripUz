from django.db import models
from django.conf import settings
from io import SEEK_CUR


from django.contrib.auth.models import AbstractUser,  Group
from django.contrib.auth.base_user import BaseUserManager
from django.db.models.deletion import SET_NULL
from django.contrib.auth.models import User 
from django.db.models.signals import post_save


class UserManager(BaseUserManager):
    def get_by_natural_key(self, username):
        return self.get(username__iexact=username)

    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)
    

class User(AbstractUser):
    phone = models.CharField(max_length=15, default=None, null=True)

    objects = UserManager()

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
#     first_name = models.CharField(max_length=100, null=True, blank=True)
#     last_name = models.CharField(max_length=100, null=True, blank=True)
#     phone = models.CharField(max_length=14, null=True, blank=True)

#     def __str__(self):
#         return self.user.username

# def create_user(sender, instance, created, **kwargs):

#     if created:
#         User.objects.create(user=instance)
#         print('Profile created!')

# post_save.connect(create_user, sender=Profile)

# def update_user(sender, instance, created, **kwargs):

#     if created == False:
#         instance.profile.save()
#         print('Profile updated!')

# post_save.connect(update_user, sender=Profile)




class Driver(models.Model):
    User = settings.AUTH_USER_MODEL
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='drivers')
    birthday = models.DateField()
    gender = models.CharField(max_length=255, choices=(('male', 'Male'), ('famale', 'Famale')))  
    smoking = models.BooleanField(default=False)
    experience = models.IntegerField(null=True)
    # driverlicence = models.ImageField()
    startDate = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.user.username

# def create_user(sender, instance, created, **kwargs):

#     if created:
#         User.objects.create(user=instance)
#         print('Profile created!')

# post_save.connect(create_user, sender=Driver)

# def update_user(sender, instance, created, **kwargs):

#     if created == False:
#         instance.profile.save()
#         print('Profile updated!')

# post_save.connect(update_user, sender=Driver)



class Bus(models.Model):
    color = (
        ('white', 'white'),
        ('green', 'green'),
        ('black', 'black'),
        ('grey', 'grey'),
        ('red', 'red'),
    )
    busNumberCodes = (
        ('Toshkent shahri', '01'),
        ('Toshkent viloyati', '10'),
        ('Samarqand viloyati', '30'),
        ("Farg'ona viloyati", '40'),
        ('Namangan viloyati', '50'),
        ('Andijon viloyati', '60'),
        ('Jizzax viloyati', '25'),
        ('Sirdaryo viloyati', '20',),
        ('Xorazm viloyati','90'),
        ('Navoiy viloyati', '85'),
        ('Qashqadaryo viloyati', '70'),
        ('Surxondaro viloyati', '75'),
        ('Buxoro viloyati', '80'),
    )
    driver=models.ForeignKey(Driver, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    code = models.CharField(max_length=50, choices=busNumberCodes)
    number = models.CharField(max_length=6, null=True)
    color = models.CharField(max_length=20, choices=color)
    seats = models.IntegerField(default=0)
    conditioner = models.BooleanField(default=False)
    image = models.ImageField(upload_to="Buses", blank=True)

    def __str__(self):
        return self.code + "|" + self.number

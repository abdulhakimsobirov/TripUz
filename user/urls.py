from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('registration/', views.UserRegistration.as_view(), name="registration"),
    path('login/', views.userLogin, name="login"),
    path('logout/', views.userLogout, name="logout"),


    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('blog/', views.blog, name="blog"),
    path('contact/', views.contact, name="contact"),
    path('portfolio', views.portfolio, name="portfolio"),
    path('team/', views.team, name="team"),
   

    path('userprofile/', views.profile, name="userprofile"),

    path('driver_registration/', views.DriverRegistration.as_view(), name="driver_registration"),
    path('bus_registration/', views.BusRegistration.as_view(), name="bus_registration")
]
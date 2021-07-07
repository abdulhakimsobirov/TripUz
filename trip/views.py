from django.shortcuts import render
from django.views import View
from .forms import *
from django.shortcuts import redirect
from .models import *
from .filters import TripFilter
from django.core.paginator import EmptyPage, Paginator
from django.views.generic.edit import CreateView
from django.utils.translation import gettext_lazy as _
from django.contrib import messages


class TripDriver(View):
    def get(self, request):
        try:
            driver = request.user.driver
        except:
            driver = False
        if driver:
            buses = Bus.objects.filter(driver=driver)
            tripform = TripForm()
            context = {'tripform': tripform, "buses": buses}
            request.title = "Work driver"
            return render(request, 'trip/trip_drivers.html', context)
        return redirect('userprofile')
    def post(self, request):
        tripform = TripForm(data=request.POST)
        try:
            if tripform.is_valid():
                tForm = tripform.save(commit=False)
                tForm.driver = request.user.driver
                tForm.save()
            
                return redirect('userprofile')
        except:
            messages.success(request, "you information incorrect...")
            return redirect('trip_driver')



        context = {'tripform': tripform}
        return render(request, 'trip/trip_drivers.html', context)

def orderTrip(request):

    ordertrip = Trip.objects.all()
    
    tfilter = TripFilter(request.GET, queryset=ordertrip)
    ordertrip = tfilter.qs
    
    mytrip = OrderTripForm()
    if request.method == "POST":
        mytrip = OrderTripForm(request.POST)
        if mytrip.is_valid():
            mytrip.save()

            return redirect('/')

    context = {'ordertrip': ordertrip, 'tfilter': tfilter, 'mytrip': mytrip}
    return render(request, 'trip/ordertrip.html', context)


# --------------------------------------MAP-----------------------------------

class AddressView(CreateView):

    model = Station
    fields = ['address']
    template_name = 'user/home.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['token'] = 'pk.eyJ1IjoidHVuYWhvYmJ5IiwiYSI6ImNra3IwaDNxcTBtbzAycm81dTFpOWhvcjAifQ.8ixXcuSDUuAlDSlazSLMCA'
        context['addresses'] = Station.objects.all()
        return context



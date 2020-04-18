from django.shortcuts import render
from .models import City 
from django.views.generic.detail import DetailView

def home(request):
    cities = City.objects.all()  
    return render(request, 'cities/home.html', {'objects_list': cities}) 

class CityDetailView(DetailView):
    queryset = City.objects.all()
    context_object_name ='objects'
    template_name = 'cities/detail.html'
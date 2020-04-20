from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .forms import CityForm
from .models import City 

def home(request):
    if request.method == 'POST':
        form = CityForm(request.POST or None)
        if form.is_valid():
            print(form.cleaned_data)
    form = CityForm()
    # print(request.POST)
    city = request.POST.get('name')
    # print(city)
    cities = City.objects.all()  
    return render(request, 'cities/home.html', {'objects_list': cities, 'form': form}) 

class CityDetailView(DetailView):
    queryset = City.objects.all()
    context_object_name ='objects'
    template_name = 'cities/detail.html'

class CityCreateView(CreateView):
    model = City
    form_class = CityForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('city:home')


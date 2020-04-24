from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.core.paginator import Paginator
from django.urls import reverse_lazy

from .forms import CityForm
from .models import City 

def home(request):
    # if request.method == 'POST':
    #     form = CityForm(request.POST or None)
    #     if form.is_valid():
    #         print(form.cleaned_data)
    # form = CityForm()
    # # print(request.POST)
    # city = request.POST.get('name')
    # # print(city)
    cities = City.objects.all()  
    paginator = Paginator(cities, 3) 
    page = request.GET.get('page')
    cities = paginator.get_page(page)
    return render(request, 'cities/home.html', {'objects_list': cities,}) 

class CityDetailView(DetailView):
    queryset = City.objects.all()
    context_object_name ='objects'
    template_name = 'cities/detail.html'

class CityCreateView(SuccessMessageMixin, CreateView):
    model = City
    form_class = CityForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('city:home')
    success_message = 'Город успешно создан.'

class CityUpdateView(SuccessMessageMixin, UpdateView):
    model = City
    form_class = CityForm
    template_name = 'cities/Update.html'
    success_url = reverse_lazy('city:home')
    success_message = 'Город отредактирован.'

class CityDeleteView(DeleteView):
    model = City
    # template_name = 'cities/Delete.html'
    success_url = reverse_lazy('city:home')

    # для моментального удаления объекта, без запроса подтверждения на 
    # отдельной форме html
    def get(self,request,*args, **kwargs):
        messages.success(request, 'Город удален')
        return self.post(request, *args, **kwargs)
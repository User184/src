from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Train

def home(request):
    trains = Train.objects.all()  
    paginator = Paginator(trains, 3) 
    page = request.GET.get('page')
    trains = paginator.get_page(page)
    return render(request, 'trains/home.html', {'objects_list': trains,}) 

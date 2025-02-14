from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy

from .models import Train
from .forms import TrainForm


def home(request):
    trains = Train.objects.all()  
    paginator = Paginator(trains, 8) 
    page = request.GET.get('page')
    trains = paginator.get_page(page)
    return render(request, 'trains/home.html', {'objects_list': trains, }) 

class TrainCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Train
    form_class = TrainForm
    template_name = 'trains/create.html'
    success_url = reverse_lazy('train:home')
    success_message = 'Поезд успешно создан.'

class TrainDetailView(DetailView):
    queryset = Train.objects.all()
    context_object_name ='objects'
    template_name = 'trains/detail.html'

class TrainUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = Train
    form_class = TrainForm
    template_name = 'trains/update.html'
    success_url = reverse_lazy('train:home')
    success_message = 'Номер поезда отредактирован.'

class TrainDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = Train
    # template_name = 'trains/Delete.html'
    success_url = reverse_lazy('train:home')

    # для моментального удаления объекта, без запроса подтверждения на 
    # отдельной форме html
    def get(self,request,*args, **kwargs):
        messages.success(request, 'Поезд удален')
        return self.post(request, *args, **kwargs)
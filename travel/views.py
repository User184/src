from django.shortcuts import render

def home_view(request):
    context = {'name': 'Dave'}
    
    return render(request, 'home.html',context) 
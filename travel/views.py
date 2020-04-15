from django.shortcuts import render

def home_view(request):
    context = {'name': 'Yurii'}
    
    return render(request, 'home.html',context) 
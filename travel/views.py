from django.shortcuts import render

def home_view(request):
    context = {'name': 'Mark'}
    
    return render(request, 'home.html',context) 
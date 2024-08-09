# innovexnepalwebsite/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'innovexnepalwebsite/index.html')

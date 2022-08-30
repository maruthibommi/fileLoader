from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Hello, Django!")

def hello_there(request):
    return render(request,'fileLoad/Html_css_files/mainLoad.html')
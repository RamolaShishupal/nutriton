
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.

def base(request):
    return render(request,'nutri/base.html')

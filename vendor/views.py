from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request) :
  return render(request, 'index.html')

def dashboard(request): 
  return(render(request, 'vendor/vendordashboard.html'))

def chart(request): 
  return(render(request, 'vendor/pages/charts/chartjs.html'))

def table(request): 
  return(render(request, 'vendor/pages/tables/basic-table.html'))


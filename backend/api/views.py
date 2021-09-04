from django.shortcuts import render
from django.views import generic

class testView(generic.CreateView):
  template_name = 'home.html'
from django.shortcuts import render
from django.views.generic import TemplateView
from resturant.models import * 

class HomePageView(TemplateView):
    template_name = 'home.html'

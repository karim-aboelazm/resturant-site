from django.shortcuts import render
from django.views.generic import TemplateView
from resturant.models import * 

class HomePageView(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["resturant"] = Resturant.objects.latest('id')
        return context
    

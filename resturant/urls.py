from django.urls import path
from resturant.views import *

app_name = "resturant"

urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
]
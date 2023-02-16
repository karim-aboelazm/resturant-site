from django.contrib import admin
from .models import *
rest_models=[
Resturant,
ResturantSiteImages,
ResturantGalaryImages,
ResturantChifs,
ResturantTestimonials,
ResturantClient,
ResturantTableReservasion,
ResturantEvents,
ResturantSpecials,
ResturantWhyUs,
ResturantAboutPlace,
ResturantMenuCategory,
ResturantMenu,
ResturantCart,
ResturantMenuCart,
ResturantMenuOrder,
]
for model in rest_models:
    admin.site.register(model)

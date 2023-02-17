from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import *

admin.site.site_header = _("Resturant Adminstration")
admin.site.site_title = _("Resturant Admin Portal")
admin.site.index_title = _("Welcome to Our Admin")

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

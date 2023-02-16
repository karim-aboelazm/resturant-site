from django.contrib import admin
from django.urls import path,include
# importing settings and static urls 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    # include urls from resturant app in urls in project
    path('',include("resturant.urls",namespace='restu'))
]

# add static files if debug is True
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
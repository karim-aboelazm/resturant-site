#--------------------------------------------------------
#    Importing Libraries and using py files in project
#--------------------------------------------------------

from django.contrib.auth.models import User
from .models import *
from rest_framework import serializers

# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')
        
# Admin serializer     
class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResturantAdmins
        fields = '__all__'
        
# Client serializer       
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResturantClient
        fields = ('id', 'user', 'full_name', 'address', 'image','phone')

# resturant serializer
class ResturantSerializer(serializers.ModelSerializer):
    class Meta:
       model = Resturant
       fields = '__all__'

# resturant place serializer 
class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
       model = ResturantAboutPlace
       fields = '__all__'
       
# resturant place images serializer 
class SiteImagesSerializer(serializers.ModelSerializer):
    class Meta:
       model = ResturantSiteImages
       fields = '__all__'

# resturant galary serializer 
class GalarySerializer(serializers.ModelSerializer):
    class Meta:
       model = ResturantGalaryImages
       fields = '__all__'

# resturant chefs serializer 
class ChefsSerializer(serializers.ModelSerializer):
    class Meta:
       model = ResturantChifs
       fields = '__all__'

# resturant testimonials serializer
class TestimonialsSerializer(serializers.ModelSerializer):
    class Meta:
       model = ResturantTestimonials
       fields = '__all__'

# resturant tabels serializer
class TabelsSerializer(serializers.ModelSerializer):
    class Meta:
       model = ResturantTableReservasion
       fields = '__all__'

# resturant events serializer
class EventsSerializer(serializers.ModelSerializer):
    class Meta:
       model = ResturantEvents
       fields = '__all__'

# resturant specials serializer
class SpecialsSerializer(serializers.ModelSerializer):
    class Meta:
       model = ResturantSpecials
       fields = '__all__'

# resturant whyus serializer
class WhyUsSerializer(serializers.ModelSerializer):
    class Meta:
       model = ResturantWhyUs
       fields = '__all__'

# resturant menu category serializer
class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
       model = ResturantMenuCategory
       fields = '__all__'

# resturant menu category serializer
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
       model = ResturantMenu
       fields = '__all__'

# resturant cart serializer
class CartSerializer(serializers.ModelSerializer):
    class Meta:
       model = ResturantCart
       fields = '__all__'

# resturant menu cart serializer
class MenuCartSerializer(serializers.ModelSerializer):
    class Meta:
       model = ResturantMenuCart
       fields = '__all__'

# resturant order serializer
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
       model = ResturantMenuOrder
       fields = '__all__'

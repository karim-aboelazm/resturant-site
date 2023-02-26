#--------------------------------------------------------
#    Importing Libraries and using py files in project
#--------------------------------------------------------

from .models import *
from .serializers import *
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

#--------------------------------------------------------
#                     Resturant USER API
#--------------------------------------------------------

# All Users Retrive Api
class UserListApi(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer 
    
# User Detail Api
class UserDetailApi(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
# User filter search Api     
class UserFilterApi(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,kw,format=None):
        user = User.objects.filter(
            Q(username__icontains=kw)|
            Q(email__icontains=kw)|
            Q(first_name__icontains=kw)|
            Q(last_name__icontains=kw))
        serializer = UserSerializer(user,many=True,context={'request':request})
        return Response({'user_filter':serializer.data}) 

#--------------------------------------------------------
#                     Resturant Admin API
#--------------------------------------------------------

# All Admins Retrive Api
class AdminListApi(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ResturantAdmins.objects.all()
    serializer_class = AdminSerializer
    
# Admin Detail Api
class AdminDetailApi(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ResturantAdmins.objects.all()
    serializer_class = AdminSerializer
  
# Admin filter search Api  
class AdminFilterApi(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,kw,format=None):
        admin = ResturantAdmins.objects.filter(
            Q(user__uername__icontains=kw)|
            Q(full_name__icontains=kw)|
            Q(mobile__icontains=kw))
        serializer = AdminSerializer(admin,many=True,context={'request':request})
        return Response({'admin_filter':serializer.data})

#--------------------------------------------------------
#                    Resturant Client API
#--------------------------------------------------------

# All Client Retrive Api
class ClientListApi(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ResturantClient.objects.all()
    serializer_class = ClientSerializer

# Client details Api
class ClientDetailApi(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ResturantClient.objects.all()
    serializer_class = ClientSerializer

# Client filter search Api
class ClientFilterApi(APIView):
    permission_classes = [IsAuthenticated]
    def get(eslf,request,kw,format=None):
        client = ResturantClient.objects.filter(
            Q(user__uername__icontains=kw)|
            Q(full_name__icontains=kw)|
            Q(phone__icontains=kw)|
            Q(address__icontains=kw))
        serializer = ClientSerializer(client,many=True,context={'request':request})
        return Response({'client_filter':serializer.data}) 

#--------------------------------------------------------
#                      Resturant API
#--------------------------------------------------------

# ALl Resturant Retrive Api
class ResturantApi(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,format=None):
        resturant = Resturant.objects.all()
        serializer = ResturantSerializer(resturant,many=True,context={'request':request})
        return Response({'resturant':serializer.data})

# Resturant details Api
class ResturantDetailApi(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Resturant.objects.all()
    serializer_class = ResturantSerializer

# Resturant filter search Api
class ResturantFilterApi(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,kw,format=None):
        resturant = Resturant.objects.filter(
                    Q(title_en__icontains=kw)|
                    Q(description_en__icontains=kw)|
                    Q(opening_sentence_en__icontains=kw)|
                    Q(address_en__icontains=kw)|
                    Q(phone_num__icontains=kw)|
                    Q(email_address__icontains=kw)|
                    Q(title_ar__icontains=kw)|
                    Q(description_ar__icontains=kw)|
                    Q(opening_sentence_ar__icontains=kw)|
                    Q(address_ar__icontains=kw))
        serializer = ResturantSerializer(resturant,many=True,context={'request':request})
        return Response({'resturant_filter':serializer.data}) 

#--------------------------------------------------------
#                      Resturant Place API
#--------------------------------------------------------

# ALl Resturant Place Retrive Api
class ResturantPlaceApi(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,format=None):
        resturantplace = ResturantAboutPlace.objects.all()
        serializer = PlaceSerializer(resturantplace,many=True,context={'request':request})
        return Response({'resturant_place':serializer.data})

# Resturant Place details Api
class ResturantPlaceDetailApi(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ResturantAboutPlace.objects.all()
    serializer_class = PlaceSerializer

# Resturant Place filter search Api
class ResturantPlaceFilterApi(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,kw,format=None):
        resturantplace = ResturantAboutPlace.objects.filter(
                    Q(title_en__icontains=kw)|
                    Q(description_en__icontains=kw)|
                    Q(title_ar__icontains=kw)|
                    Q(description_ar__icontains=kw))
        serializer = PlaceSerializer(resturantplace,many=True,context={'request':request})
        return Response({'resturant_place_filter':serializer.data}) 

#--------------------------------------------------------
#                      Resturant Place Images API
#--------------------------------------------------------

# ALl Resturant Place Images Retrive Api
class ResturantPlaceImagesApi(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,format=None):
        resturant_place_image = ResturantSiteImages.objects.all()
        serializer = SiteImagesSerializer(resturant_place_image,many=True,context={'request':request})
        return Response({'resturant_place_image':serializer.data})

# Resturant Place Images details Api
class ResturantPlaceImagesDetailApi(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ResturantSiteImages.objects.all()
    serializer_class = SiteImagesSerializer

#--------------------------------------------------------
#                      Resturant Galary API
#--------------------------------------------------------

# ALl Resturant Galary Images Retrive Api
class ResturantGalaryApi(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,format=None):
        resturant_galary = ResturantGalaryImages.objects.all()
        serializer = GalarySerializer(resturant_galary,many=True,context={'request':request})
        return Response({'resturant_galary':serializer.data})

# Resturant Galary Images details Api
class ResturantGalaryDetailApi(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ResturantGalaryImages.objects.all()
    serializer_class = GalarySerializer

#--------------------------------------------------------
#                    Resturant Chef API
#--------------------------------------------------------

# All Chefs Retrive Api
class ChefsListApi(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ResturantChifs.objects.all()
    serializer_class = ChefsSerializer

# Chefs details Api
class ChefsDetailApi(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ResturantChifs.objects.all()
    serializer_class = ChefsSerializer

# Chefs filter search Api
class ChefsFilterApi(APIView):
    permission_classes = [IsAuthenticated]
    def get(eslf,request,kw,format=None):
        chef = ResturantChifs.objects.filter(
            Q(chif_name_en__icontains=kw)|
            Q(chif_proffesion_en__icontains=kw)|
            Q(chif_name_ar__icontains=kw)|
            Q(chif_proffesion_ar__icontains=kw))
        serializer = ChefsSerializer(chef,many=True,context={'request':request})
        return Response({'chef_filter':serializer.data}) 

#--------------------------------------------------------
#                    Resturant testimonials API
#--------------------------------------------------------

# All testimonials Retrive Api
class TestimonialsListApi(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ResturantTestimonials.objects.all()
    serializer_class = TestimonialsSerializer

# testimonials details Api
class TestimonialsDetailApi(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ResturantTestimonials.objects.all()
    serializer_class = TestimonialsSerializer

# testimonials filter search Api
class TestimonialsFilterApi(APIView):
    permission_classes = [IsAuthenticated]
    def get(eslf,request,kw,format=None):
        testimonial = ResturantTestimonials.objects.filter(
            Q(name_en__icontains=kw)|
            Q(proffesion_en__icontains=kw)|
            Q(quote_en__icontains=kw)|
            Q(name_ar__icontains=kw)|
            Q(proffesion_ar__icontains=kw)|
            Q(quote_ar__icontains=kw))
        serializer = TestimonialsSerializer(testimonial,many=True,context={'request':request})
        return Response({'testimonial_filter':serializer.data}) 

#--------------------------------------------------------
#                    Resturant Tabels API
#--------------------------------------------------------

# All Tabels Retrive Api
class TabelsListApi(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ResturantTableReservasion.objects.all()
    serializer_class = TabelsSerializer

# Tabels details Api
class TabelsDetailApi(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ResturantTableReservasion.objects.all()
    serializer_class = TabelsSerializer

# Tabels filter search Api
class TabelsFilterApi(APIView):
    permission_classes = [IsAuthenticated]
    def get(eslf,request,kw,format=None):
        table = ResturantTableReservasion.objects.filter(
            Q(full_name__icontains=kw)|
            Q(email_address__icontains=kw)|
            Q(phone_number__icontains=kw)|
            Q(date__icontains=kw)|
            Q(time__icontains=kw)|
            Q(number_of_people__icontains=kw)|
            Q(message__icontains=kw))
        serializer = TabelsSerializer(table,many=True,context={'request':request})
        return Response({'table_filter':serializer.data}) 

#--------------------------------------------------------
#                    Resturant Events API
#--------------------------------------------------------

# All Events Retrive Api
class EventsListApi(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ResturantEvents.objects.all()
    serializer_class = EventsSerializer

# Events details Api
class EventsDetailApi(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ResturantEvents.objects.all()
    serializer_class = EventsSerializer

# Events filter search Api
class EventsFilterApi(APIView):
    permission_classes = [IsAuthenticated]
    def get(eslf,request,kw,format=None):
        event = ResturantEvents.objects.filter(
            Q(title_en__icontains=kw)|
            Q(description_en__icontains=kw)|
            Q(title_ar__icontains=kw)|
            Q(description_ar__icontains=kw)|
            Q(price__icontains=kw))
        serializer = EventsSerializer(event,many=True,context={'request':request})
        return Response({'event_filter':serializer.data}) 

#--------------------------------------------------------
#                    Resturant Specials API
#--------------------------------------------------------

# All Specials Retrive Api
class SpecialsListApi(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ResturantSpecials.objects.all()
    serializer_class = SpecialsSerializer

# Specials details Api
class SpecialsDetailApi(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ResturantSpecials.objects.all()
    serializer_class = SpecialsSerializer

# Specials filter search Api
class SpecialsFilterApi(APIView):
    permission_classes = [IsAuthenticated]
    def get(eslf,request,kw,format=None):
        special = ResturantSpecials.objects.filter(
            Q(category_en__icontains=kw)|
            Q(title_en__icontains=kw)|
            Q(description_en__icontains=kw)|
            Q(category_ar__icontains=kw)|
            Q(title_ar__icontains=kw)|
            Q(description_ar__icontains=kw))
        serializer = SpecialsSerializer(special,many=True,context={'request':request})
        return Response({'special_filter':serializer.data}) 

#--------------------------------------------------------
#                    Resturant WhyUs API
#--------------------------------------------------------

# All WhyUs Retrive Api
class WhyUsListApi(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ResturantWhyUs.objects.all()
    serializer_class = WhyUsSerializer

# WhyUs details Api
class WhyUsDetailApi(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ResturantWhyUs.objects.all()
    serializer_class = WhyUsSerializer

# WhyUs filter search Api
class WhyUsFilterApi(APIView):
    permission_classes = [IsAuthenticated]
    def get(eslf,request,kw,format=None):
        why = ResturantWhyUs.objects.filter(
            Q(title_en__icontains=kw)|
            Q(description_en__icontains=kw)|
            Q(title_ar__icontains=kw)|
            Q(description_ar__icontains=kw)|
            Q(title_ar__icontains=kw))
        serializer = WhyUsSerializer(why,many=True,context={'request':request})
        return Response({'why_filter':serializer.data}) 

#--------------------------------------------------------
#                    Resturant MenuCategory API
#--------------------------------------------------------

# All MenuCategory Retrive Api
class MenuCategoryListApi(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ResturantMenuCategory.objects.all()
    serializer_class = MenuCategorySerializer

# MenuCategory details Api
class MenuCategoryDetailApi(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ResturantMenuCategory.objects.all()
    serializer_class = MenuCategorySerializer

# MenuCategory filter search Api
class MenuCategoryFilterApi(APIView):
    permission_classes = [IsAuthenticated]
    def get(eslf,request,kw,format=None):
        category = ResturantMenuCategory.objects.filter(
            Q(title_en__icontains=kw)|
            Q(title_ar__icontains=kw)|
            Q(title_ar__icontains=kw))
        serializer = MenuCategorySerializer(category,many=True,context={'request':request})
        return Response({'category_filter':serializer.data}) 

#--------------------------------------------------------
#                    Resturant Menu API
#--------------------------------------------------------

# All Menu Retrive Api
class MenuListApi(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ResturantMenu.objects.all()
    serializer_class = MenuSerializer

# Menu details Api
class MenuDetailApi(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ResturantMenu.objects.all()
    serializer_class = MenuSerializer

# Menu filter search Api
class MenuFilterApi(APIView):
    permission_classes = [IsAuthenticated]
    def get(eslf,request,kw,format=None):
        menu = ResturantMenu.objects.filter(
            Q(category__title_en__icontains=kw)|
            Q(category__title_ar__icontains=kw)|
            Q(title_en__icontains=kw)|
            Q(description_en__icontains=kw)|
            Q(title_ar__icontains=kw)|
            Q(description_ar__icontains=kw)|
            Q(price__icontains=kw))
        serializer = MenuSerializer(menu,many=True,context={'request':request})
        return Response({'menu_filter':serializer.data}) 

#--------------------------------------------------------
#                    Resturant Cart API
#--------------------------------------------------------

# All Cart Retrive Api
class CartListApi(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ResturantCart.objects.all()
    serializer_class = CartSerializer

# Cart details Api
class CartDetailApi(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ResturantCart.objects.all()
    serializer_class = CartSerializer

# Cart filter search Api
class CartFilterApi(APIView):
    permission_classes = [IsAuthenticated]
    def get(eslf,request,kw,format=None):
        cart = ResturantCart.objects.filter(
            Q(user__uername__icontains=kw)|
            Q(total__icontains=kw))
        serializer = CartSerializer(cart,many=True,context={'request':request})
        return Response({'cart_filter':serializer.data}) 

#--------------------------------------------------------
#                    Resturant MenuCart API
#--------------------------------------------------------

# All MenuCart Retrive Api
class MenuCartListApi(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ResturantMenuCart.objects.all()
    serializer_class = MenuCartSerializer

# MenuCart details Api
class MenuCartDetailApi(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ResturantMenuCart.objects.all()
    serializer_class = MenuCartSerializer

# MenuCart filter search Api
class MenuCartFilterApi(APIView):
    permission_classes = [IsAuthenticated]
    def get(eslf,request,kw,format=None):
        menucart = ResturantMenuCart.objects.filter(
            Q(rate__icontains=kw)|
            Q(quantity__icontains=kw))
        serializer = MenuCartSerializer(menucart,many=True,context={'request':request})
        return Response({'menucart_filter':serializer.data}) 

#--------------------------------------------------------
#                    Resturant Order API
#--------------------------------------------------------

# All Order Retrive Api
class OrderListApi(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ResturantMenuOrder.objects.all()
    serializer_class = OrderSerializer

# Order details Api
class OrderDetailApi(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ResturantMenuOrder.objects.all()
    serializer_class = OrderSerializer

# Order filter search Api
class OrderFilterApi(APIView):
    permission_classes = [IsAuthenticated]
    def get(eslf,request,kw,format=None):
        order = ResturantMenuOrder.objects.filter(
            Q(user__uername__icontains=kw)|
            Q(first_name__icontains=kw)|
            Q(last_name__icontains=kw)|
            Q(phone_num__icontains=kw)|
            Q(email__icontains=kw)|
            Q(subtotal__icontains=kw)|
            Q(total__icontains=kw)|
            Q(order_status__icontains=kw))
        serializer = OrderSerializer(order,many=True,context={'request':request})
        return Response({'order_filter':serializer.data}) 
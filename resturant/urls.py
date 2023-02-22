from django.urls import path
from resturant.views import *

app_name = "resturant"

urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('client-register/',ResturantClientRegisterView.as_view(),name='client_register'),
    path('client-login/',ResturantClientLoginView.as_view(),name='client_login'),
    path('client-logout/',ResturantClientLogoutView.as_view(),name='client_logout'),
    
    path('forgot-password/',ForgotPasswordView.as_view(),name="forgot_password"),
    path('change-password/<int:pk>/',ChangePasswordView.as_view(),name="change_password"),
    path('reset-password/<email>/<token>/',ResetPasswordView.as_view(),name="reset_password"),
    # cart url
    path('my-dish/',CartView.as_view(),name='my_cart'),
    path('add-to-dish/<int:pk>/',AddToCartView.as_view(),name='add_to_cart'),
    path('manage-dish/<int:pk>/',ManageCartView.as_view(),name='manage_cart'),
    path('empty-dish/',EmptyCartView.as_view(),name='empty_cart'),
     # check out url
    path('check-out/',CheckOutView.as_view(),name='check_out'),
]
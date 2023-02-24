from django.urls import path
from resturant.views import *

app_name = "resturant"

urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('client-register/',ResturantClientRegisterView.as_view(),name='client_register'),
    path('client-login/',ResturantClientLoginView.as_view(),name='client_login'),
    path('client-logout/',ResturantClientLogoutView.as_view(),name='client_logout'),
    # client auth urls
    path('forgot-password/',ForgotPasswordView.as_view(),name="forgot_password"),
    path('change-password/<int:pk>/',ChangePasswordView.as_view(),name="change_password"),
    path('reset-password/<email>/<token>/',ResetPasswordView.as_view(),name="reset_password"),
    # cart urls
    path('my-dish/',CartView.as_view(),name='my_cart'),
    path('add-to-dish/<int:pk>/',AddToCartView.as_view(),name='add_to_cart'),
    path('manage-dish/<int:pk>/',ManageCartView.as_view(),name='manage_cart'),
    path('empty-dish/',EmptyCartView.as_view(),name='empty_cart'),
    # check out url
    path('check-out/',CheckOutView.as_view(),name='check_out'),
    # Admins urls
    path("admin-login/", AdminLoginView.as_view(), name="admin_login"),
    path("admin-home/", AdminHomeView.as_view(), name="admin_home"),
    path("admin-order/<int:pk>/", AdminOrderDetailView.as_view(), name="admin_order_detail"),
    path("admin-table/<int:pk>/", AdminTableDetailView.as_view(), name="admin_table_detail"),
    path("admin-all-orders/", AdminAllOrderView.as_view(), name="admin_all_order"),
    path("admin-order-<int:pk>-change/", AdminOrderStatusChangeView.as_view(), name="admin_order_status_change"),
    path("admin-table-<int:pk>-confirm/", AdminTableConfirmationView.as_view(), name="admin_table_confirm"),
    path("admin-menu-list/",AdminMenuList.as_view(), name="admin_menu_list"),
    path("admin-table-list/",AdminTablesList.as_view(), name="admin_table_list"),
    path("admin-add-menu-items/",AdminMenuAdd.as_view(), name="admin_add_menu_items"),
    path("admin-add-menu-category/",AdminCategoryAdd.as_view(), name="admin_add_menu_category"),
    path('admin-logout/',AdminLogoutView.as_view(),name='admin_logout'),
]
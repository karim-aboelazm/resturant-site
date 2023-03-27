from django.urls import path
from resturant.views import *
from resturant.api import *


app_name = "resturant"

urlpatterns = [
    # home url
    path(''                                  ,HomePageView.as_view()                    ,name='home'                        ),
    # client auth urls
    path('client-register/'                  ,ResturantClientRegisterView.as_view()     ,name='client_register'             ),
    path('client-login/'                     ,ResturantClientLoginView.as_view()        ,name='client_login'                ),
    path('client-logout/'                    ,ResturantClientLogoutView.as_view()       ,name='client_logout'               ),
    path('forgot-password/'                  ,ForgotPasswordView.as_view()              ,name="forgot_password"             ),
    path('change-password/<int:pk>/'         ,ChangePasswordView.as_view()              ,name="change_password"             ),
    path('reset-password/<email>/<token>/'   ,ResetPasswordView.as_view()               ,name="reset_password"              ),
    # cart urls
    path('my-dish/'                          ,CartView.as_view()                        ,name='my_cart'                     ),
    path('add-to-dish/<int:pk>'  ,AddToCartView.as_view()                   ,name='add_to_cart'                 ),
    path('manage-dish/<int:pk>/'             ,ManageCartView.as_view()                  ,name='manage_cart'                 ),
    path('empty-dish/'                       ,EmptyCartView.as_view()                   ,name='empty_cart'                  ),
    # check out url
    path('check-out/'                        ,CheckOutView.as_view()                    ,name='check_out'                   ),
    # Admins urls
    path("admin-login/"                      ,AdminLoginView.as_view()                  ,name="admin_login"                 ),
    path("admin-home/"                       ,AdminHomeView.as_view()                   ,name="admin_home"                  ),
    path("admin-order/<int:pk>/"             ,AdminOrderDetailView.as_view()            ,name="admin_order_detail"          ),
    path("admin-table/<int:pk>/"             ,AdminTableDetailView.as_view()            ,name="admin_table_detail"          ),
    path("admin-all-orders/"                 ,AdminAllOrderView.as_view()               ,name="admin_all_order"             ),
    path("admin-order-<int:pk>-change/"      ,AdminOrderStatusChangeView.as_view()      ,name="admin_order_status_change"   ),
    path("admin-table-<int:pk>-confirm/"     ,AdminTableConfirmationView.as_view()      ,name="admin_table_confirm"         ),
    path("admin-menu-list/"                  ,AdminMenuList.as_view()                   ,name="admin_menu_list"             ),
    path("admin-table-list/"                 ,AdminTablesList.as_view()                 ,name="admin_table_list"            ),
    path("admin-add-menu-items/"             ,AdminMenuAdd.as_view()                    ,name="admin_add_menu_items"        ),
    path("admin-add-menu-category/"          ,AdminCategoryAdd.as_view()                ,name="admin_add_menu_category"     ),
    path('admin-logout/'                     ,AdminLogoutView.as_view()                 ,name='admin_logout'                ),
    # user api urls 
    path('api/user-list/'                    ,UserListApi.as_view()                     ,name='api_user_list'               ),
    path('api/user-detail/<int:pk>'          ,UserDetailApi.as_view()                   ,name='api_user_detail'             ),
    path('api/user-filter/<str:kw>'          ,UserFilterApi.as_view()                   ,name='api_user_filter'             ),
    # admin api urls
    path('api/admin-list/'                   ,AdminListApi.as_view()                    ,name='api_admin_list'              ),
    path('api/admin-detail/<int:pk>'         ,AdminDetailApi.as_view()                  ,name='api_admin_detail'            ),
    path('api/admin-filter/<str:kw>'         ,AdminFilterApi.as_view()                  ,name='api_admin_filter'            ),
    # client api urls
    path('api/client-list/'                  ,ClientListApi.as_view()                   ,name='api_client_list'             ),
    path('api/client-detail/<int:pk>'        ,ClientDetailApi.as_view()                 ,name='api_client_detail'           ),
    path('api/client-filter/<str:kw>'        ,ClientFilterApi.as_view()                 ,name='api_client_filter'           ),
    # resturant api urls
    path('api/resturant-list/'               ,ResturantApi.as_view()                    ,name='api_resturant_list'          ),
    path('api/resturant-detail/<int:pk>'     ,ResturantDetailApi.as_view()              ,name='api_resturant_detail'        ),
    path('api/resturant-filter/<str:kw>'     ,ResturantFilterApi.as_view()              ,name='api_resturant_filter'        ),
    # resturant place api urls
    path('api/place-list/'                   ,ResturantPlaceApi.as_view()               ,name='api_place_list'              ),
    path('api/place-detail/<int:pk>'         ,ResturantPlaceDetailApi.as_view()         ,name='api_place_detail'            ),
    path('api/place-filter/<str:kw>'         ,ResturantPlaceFilterApi.as_view()         ,name='api_place_filter'            ),
    # resturant place images api urls
    path('api/place-images-list/'            ,ResturantPlaceImagesApi.as_view()         ,name='api_place_images_list'       ),
    path('api/place-images-detail/<int:pk>'  ,ResturantPlaceImagesDetailApi.as_view()   ,name='api_place_images_detail'     ),
    # resturant galary api urls
    path('api/galary-list/'                  ,ResturantGalaryApi.as_view()              ,name='api_galary_list'             ),
    path('api/galary-detail/<int:pk>'        ,ResturantGalaryDetailApi.as_view()        ,name='api_galary_detail'           ),
    # resturant chef api urls
    path('api/chef-list/'                    ,ChefsListApi.as_view()                    ,name='api_chef_list'               ),
    path('api/chef-detail/<int:pk>'          ,ChefsDetailApi.as_view()                  ,name='api_chef_detail'             ),
    path('api/chef-filter/<str:kw>'          ,ChefsFilterApi.as_view()                  ,name='api_chef_filter'             ),
    # resturant chef api urls
    path('api/testimonials-list/'            ,TestimonialsListApi.as_view()             ,name='api_testimonials_list'       ),
    path('api/testimonials-detail/<int:pk>'  ,TestimonialsDetailApi.as_view()           ,name='api_testimonials_detail'     ),
    path('api/testimonials-filter/<str:kw>'  ,TestimonialsFilterApi.as_view()           ,name='api_testimonials_filter'     ),
    # resturant tables api urls
    path('api/table-list/'                   ,TabelsListApi.as_view()                   ,name='api_table_list'              ),
    path('api/table-detail/<int:pk>'         ,TabelsDetailApi.as_view()                 ,name='api_table_detail'            ),
    path('api/table-filter/<str:kw>'         ,TabelsFilterApi.as_view()                 ,name='api_table_filter'            ),
    # resturant events api urls
    path('api/event-list/'                   ,EventsListApi.as_view()                   ,name='api_event_list'              ),
    path('api/event-detail/<int:pk>'         ,EventsDetailApi.as_view()                 ,name='api_event_detail'            ),
    path('api/event-filter/<str:kw>'         ,EventsFilterApi.as_view()                 ,name='api_event_filter'            ),
    # resturant specials api urls
    path('api/special-list/'                 ,SpecialsListApi.as_view()                 ,name='api_special_list'            ),
    path('api/special-detail/<int:pk>'       ,SpecialsDetailApi.as_view()               ,name='api_special_detail'          ),
    path('api/special-filter/<str:kw>'       ,SpecialsFilterApi.as_view()               ,name='api_special_filter'          ),
    # resturant WhyUs api urls
    path('api/whyus-list/'                   ,WhyUsListApi.as_view()                    ,name='api_whyus_list'              ),
    path('api/whyus-detail/<int:pk>'         ,WhyUsDetailApi.as_view()                  ,name='api_whyus_detail'            ),
    path('api/whyus-filter/<str:kw>'         ,WhyUsFilterApi.as_view()                  ,name='api_whyus_filter'            ),
    # resturant MenuCategory api urls
    path('api/menu-category-list/'           ,MenuCategoryListApi.as_view()             ,name='api_menu_category_list'      ),
    path('api/menu-category-detail/<int:pk>' ,MenuCategoryDetailApi.as_view()           ,name='api_menu_category_detail'    ),
    path('api/menu-category-filter/<str:kw>' ,MenuCategoryFilterApi.as_view()           ,name='api_menu_category_filter'    ),
    # resturant Menu api urls
    path('api/menu-list/'                    ,MenuListApi.as_view()                     ,name='api_menu_list'               ),
    path('api/menu-detail/<int:pk>'          ,MenuDetailApi.as_view()                   ,name='api_menu_detail'             ),
    path('api/menu-filter/<str:kw>'          ,MenuFilterApi.as_view()                   ,name='api_menu_filter'             ),
    # resturant cart api urls
    path('api/cart-list/'                    ,CartListApi.as_view()                     ,name='api_cart_list'               ),
    path('api/cart-detail/<int:pk>'          ,CartDetailApi.as_view()                   ,name='api_cart_detail'             ),
    path('api/cart-filter/<str:kw>'          ,CartFilterApi.as_view()                   ,name='api_cart_filter'             ),
    # resturant Menu cart api urls
    path('api/menu-cart-list/'               ,MenuCartListApi.as_view()                 ,name='api_menu_cart_list'          ),
    path('api/menu-cart-detail/<int:pk>'     ,MenuCartDetailApi.as_view()               ,name='api_menu_cart_detail'        ),
    path('api/menu-cart-filter/<str:kw>'     ,MenuCartFilterApi.as_view()               ,name='api_menu_cart_filter'        ),
    # resturant order api urls
    path('api/order-list/'                   ,OrderListApi.as_view()                    ,name='api_order_list'              ),
    path('api/order-detail/<int:pk>'         ,OrderDetailApi.as_view()                  ,name='api_order_detail'            ),
    path('api/order-filter/<str:kw>'         ,OrderFilterApi.as_view()                  ,name='api_order_filter'            ),
    
    
    
]
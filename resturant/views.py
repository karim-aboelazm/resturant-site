from django.views.generic import TemplateView,View,CreateView,FormView,DetailView,ListView,UpdateView
from django.contrib.auth import authenticate , login ,logout
from django.contrib.auth.views import PasswordChangeView
from django.utils.translation import gettext_lazy as _
from django.shortcuts import render,redirect,reverse
from django.shortcuts import render,redirect
from .utils import password_reset_token
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.conf import settings
from resturant.models import * 
from django.views import View
from .forms import *

# ----------------------------------------------------
# ----------------------------------------------------

class AdminRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and ResturantAdmins.objects.filter(user=request.user).exists():
            pass
        else:
            return redirect("/admin-login/")
        return super().dispatch(request, *args, **kwargs)

class AdminLoginView(FormView):
    template_name = "Admins/admin_login.html"
    form_class = AdminLoginForm
    success_url = reverse_lazy('restu:admin_home')
    
    def form_valid(self, form):
        user_name = form.cleaned_data.get('username')
        pass_word = form.cleaned_data['password']
        usr = authenticate(username=user_name,password=pass_word)
        if usr is not None and ResturantAdmins.objects.filter(user=usr).exists():
            login(self.request, usr)
        else:
            return render(self.request,self.template_name,{'form':self.form_class})
        return super().form_valid(form)

class AdminHomeView(AdminRequiredMixin,TemplateView):
    template_name = "Admins/admin_home.html"
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and ResturantAdmins.objects.filter(user=request.user).exists():
            pass
        else:
            return redirect("/admin-login/?next=/admin-home/")
        return super().dispatch(request, *args, **kwargs)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_orders"] = ResturantMenuOrder.objects.filter(order_status = "Order Received").order_by('-id')
        context["all_tables"] = ResturantTableReservasion.objects.filter(confirm=False).order_by('-id')
        context["resturant"]  = Resturant.objects.latest('id') 
        return context

class AdminOrderDetailView(AdminRequiredMixin,DetailView):
    template_name = "Admins/admin_order_detail.html"
    model = ResturantMenuOrder
    context_object_name = "order_object"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ORDER_STATUS = (
        (_("Order Received"),_("Order Received")),
        (_("Order Processing"),_("Order Processing")),
        (_("Order On The Way"),_("Order On The Way")),
        (_("Order Completed"),_("Order Completed")),
        (_("Order Canceled"),_("Order Canceled")),
        )
        context["all_status"] = ORDER_STATUS
        context["resturant"]  = Resturant.objects.latest('id')
        return context
 
class AdminTableDetailView(AdminRequiredMixin,DetailView):
    template_name = "Admins/admin_table_detail.html"
    model = ResturantTableReservasion
    context_object_name = "table_object"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["resturant"]  = Resturant.objects.latest('id')
        return context

class AdminAllOrderView(AdminRequiredMixin,ListView):
    template_name = "Admins/admin_all_order.html"
    queryset = ResturantMenuOrder.objects.all().order_by('-id')
    context_object_name = "all_orders"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["resturant"]  = Resturant.objects.latest('id')
        return context

class AdminTableConfirmationView(AdminRequiredMixin,View):
    def post(self,request, *args, **kwargs):
        table_id = self.kwargs['pk']
        table_object = ResturantTableReservasion.objects.get(id=table_id)
        table_object.confirm = True
        table_object.save()
        return redirect(reverse_lazy('restu:admin_home'))

class AdminOrderStatusChangeView(AdminRequiredMixin,View):
    def post(self,request, *args, **kwargs):
        order_id = self.kwargs['pk']
        order_object = ResturantMenuOrder.objects.get(id=order_id)
        updated_status = request.POST.get('status')
        order_object.order_status = updated_status
        order_object.save()
        return redirect(reverse_lazy('restu:admin_order_detail',kwargs={'pk':order_id}))
    
class AdminMenuList(AdminRequiredMixin,ListView):
    template_name = 'Admins/admin_menu_list.html'
    queryset = ResturantMenuCategory.objects.all()
    context_object_name = "all_menu_category"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["resturant"]  = Resturant.objects.latest('id')
        return context

class AdminTablesList(AdminRequiredMixin,ListView):
    template_name = 'Admins/admin_tables_list.html'
    queryset = ResturantTableReservasion.objects.all()
    context_object_name = "all_tables"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["resturant"]  = Resturant.objects.latest('id')
        return context

class AdminCategoryAdd(AdminRequiredMixin,CreateView):
    template_name = "Admins/add_menu_category.html"
    form_class = CategoryForm
    success_url = reverse_lazy("restu:admin_menu_list")
    def form_valid(self,form):
        form.save()
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["resturant"]  = Resturant.objects.latest('id')
        return context

class AdminMenuAdd(AdminRequiredMixin,CreateView):
    template_name = "Admins/add_menu_item.html"
    form_class = MenuForm
    success_url = reverse_lazy("restu:admin_menu_list")
    def form_valid(self,form):
        form.save()
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["resturant"]  = Resturant.objects.latest('id')
        return context

class AdminLogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('restu:home')

# ----------------------------------------------------
# ----------------------------------------------------

class RestMixin():
    def dispatch(self, request, *args, **kwargs):
        cart_id = request.session.get("cart_id")
        current_user = request.user
        if cart_id:
            cart_obj = ResturantCart.objects.get(id=cart_id)
            if current_user.is_authenticated and ResturantClient.objects.filter(user=current_user).exists():
                cart_obj.customer = current_user
                cart_obj.save()
        return super().dispatch(request, *args, **kwargs)
    
class HomePageView(FormView):
    template_name = 'Resturant/home.html' 
    form_class =  TableReservasionForm
    success_url = '/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form2']             = ContactForm()
        context["resturant"]         = Resturant.objects.latest('id') if Resturant.objects.latest('id') else None
        context["about_resturant"]   = ResturantAboutPlace.objects.latest('id') if ResturantAboutPlace.objects.latest('id') else None
        context["whyus_resturant"]   = ResturantWhyUs.objects.all().order_by('-id')
        context["special_resturant"] = ResturantSpecials.objects.all().order_by('-id')
        context["events_resturant"]  = ResturantEvents.objects.all().order_by('-id')
        context["test_resturant"]    = ResturantTestimonials.objects.all().order_by('-id')
        context["galary_resturant"]  = ResturantGalaryImages.objects.all().order_by('-id')
        context["chifs_resturant"]   = ResturantChifs.objects.all().order_by('-id')
        context["category_menu_rest"]= ResturantMenuCategory.objects.all()
        return context
   
    def post(self, request, *args, **kwargs):
        form2 = ContactForm()
        if 'full_name' in request.POST:
            table_reservation_form = TableReservasionForm(request.POST)
            if table_reservation_form.is_valid():
                table_reservation_form.save()
                return super().form_valid(table_reservation_form)
            
        elif 'name' in request.POST:
            form2 = ContactForm(request.POST)
            if form2.is_valid():
                Name = form2.cleaned_data['name']
                Email = form2.cleaned_data['email']
                Subject = form2.cleaned_data['subject']
                Message = form2.cleaned_data['message']
                msg = f"""
                Hello Dear,
                    -----------
                        My Name  :{Name}
                        My email : {Email}
                        Message  : {Message}
                    ----------
                Thank You!
                """
                send_mail(
                    Subject,
                    msg,
                    Email,
                    [settings.EMAIL_HOST_USER],
                    fail_silently=False,
                )
                return redirect(self.success_url)
        
        return super().form_valid(form2)

class ResturantClientRegisterView(CreateView):
    template_name = 'Clients/signup.html'
    form_class = ResturantClientRegisterForm
    success_url = '/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["resturant"]         = Resturant.objects.latest('id')
        return context
    
    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        email    = form.cleaned_data.get('email')
        full_name = form.cleaned_data.get('full_name')
        user = User.objects.create_user(username=username,email=email,password=password,first_name=full_name.split(" ")[0],last_name=full_name.split(" ")[-1])
        form.instance.user = user
        login(self.request , user)
        return super().form_valid(form)

class ResturantClientLogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('restu:home')

class ResturantClientLoginView(FormView):
    template_name = 'Clients/login.html'
    form_class = ResturantClientLoginForm
    success_url = reverse_lazy('restu:home')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["resturant"]         = Resturant.objects.latest('id')
        return context

    def form_valid(self,form):
        user_name = form.cleaned_data.get('username')
        pass_word = form.cleaned_data['password']
        usr = authenticate(username=user_name,password=pass_word)
        if usr is not None and ResturantClient.objects.filter(user=usr).exists():
            login(self.request, usr)
        else:
            return render(self.request,self.template_name,{'form':self.form_class})
        return super().form_valid(form)
    
    def get_success_url(self):
        if 'next' in self.request.GET:
            next_url = self.request.GET.get('next')
            return next_url
        else:
            return self.success_url

'''
class ResturantClientProfileView(RestMixin,TemplateView):
    template_name = "profile.html"
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.resturantclient:
            pass
        else:
            return redirect("/client-login/?next=/client-profile/")
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["order"] = []
        context["client_items"] = []
        
        for i in self.request.user.resturantmenuorder_set.all():
            context["order"].append(i)
        for j in context["order"]:
            order_item  = ResturantMenuCart.objects.get(cart=j.cart).item
            context["client_items"].append(ResturantMenu.objects.get(id=order_item.id))
        
        context["profile"] = ResturantClient.objects.get(user=self.request.user) 
       
        context["client_items"] = list(set(context["client_items"]))[::-1]
        return context

class UpdateProfileView(RestMixin,UpdateView):
    model = ResturantClient
    form_class = ProfileUpdateForm
    template_name = 'edit_profile.html'
    
    def get_object(self, *args, **kwargs):
        customer = get_object_or_404(ResturantClient, pk=self.kwargs['pk'])
        return customer
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def get_success_url(self, *args, **kwargs):
        success_url = reverse_lazy('restu:client_profile')
        return success_url
'''

class ForgotPasswordView(FormView):
    template_name = 'Clients/forgot_password.html'
    form_class = PasswordForm
    success_url = "/forgot-password/?m=s"
    def form_valid(self,form):
        # get email from user
        email = form.cleaned_data.get("email")
        # get current host ip/Domain [127.0.0.1:8000]
        url = self.request.META['HTTP_HOST']
        # get customer and then user
        customer = ResturantClient.objects.get(user__email = email)
        user = customer.user
        # sent mail to customer with email
        text_content = 'Please click the link below to reset your password.  '
        html_content = url + "/reset-password/" + email +"/" + password_reset_token.make_token(user)+"/"
        send_mail(
            'Password Reset Link | BABA VOSS Resturant',
            text_content + html_content,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently = False,
            
        )
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["resturant"]         = Resturant.objects.latest('id')
        return context

class ResetPasswordView(FormView):
    template_name = 'Clients/reset_password.html'
    form_class = PasswordResetForm
    success_url = '/client-login/'
    
    def dispatch(self, request, *args, **kwargs):
        email = self.kwargs.get("email")
        user = User.objects.get(email=email)
        token = self.kwargs.get("token")
        if user is not None and password_reset_token.check_token(user,token):
           pass
        else:
            return redirect(reverse('restu:forgot_password')+'?m=e')
        return super().dispatch(request, *args, **kwargs)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["resturant"]         = Resturant.objects.latest('id')
       
        return context
    
    def form_valid(self,form):
        password = form.cleaned_data['new_password']
        email = self.kwargs.get("email")
        user = User.objects.get(email=email)
        user.set_password(password)
        user.save()
        return super().form_valid(form)

class ChangePasswordView(PasswordChangeView):
    template_name = 'Clients/change_password.html'
    success_url = '/'         
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["resturant"]         = Resturant.objects.latest('id')
        return context

class AddToCartView(RestMixin,TemplateView):
    template_name = "Menu/add_to_cart.html"
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.resturantclient:
            pass
        else:
            return redirect("/client-login/?next=/")
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["resturant"]= Resturant.objects.latest('id')
        item_id = kwargs['pk']
        item_obj = ResturantMenu.objects.get(id=item_id)
        context["item"] = item_obj
        cart_id = self.request.session.get('cart_id',None)
        if cart_id:
            cart = ResturantCart.objects.get(id = cart_id)
            this_item_in_cart = cart.resturantmenucart_set.filter(item=item_obj)
            if this_item_in_cart.exists():
                cartitem = this_item_in_cart.last()
                cartitem.quantity += 1
                cartitem.subtotal += item_obj.price
                cartitem.save()
                cart.total += item_obj.price
                cart.save()
            else:
                cartitem = ResturantMenuCart.objects.create(cart=cart,item=item_obj,
                                                         rate=item_obj.price,quantity=1,
                                                         subtotal=item_obj.price)
                cart.total += item_obj.price
                cart.user = self.request.user
                cart.save()
        else:
            cart = ResturantCart.objects.create(total=0)
            self.request.session['cart_id'] = cart.id
            cartitem = ResturantMenuCart.objects.create(cart=cart,item=item_obj,
                                                         rate=item_obj.price,quantity=1,
                                                         subtotal=item_obj.price)
            cart.total += item_obj.price
            cart.user = self.request.user
            cart.save()
        return context

class CartView(RestMixin,TemplateView):
    template_name = "Menu/cart.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["resturant"]         = Resturant.objects.latest('id')
        cart_id = self.request.session.get('cart_id',None)
        if cart_id:
            cart = ResturantCart.objects.get(id=cart_id)
        else:
            cart = None
        context["cart"] = cart 
        return context

class ManageCartView(RestMixin,View):
    def get(self,request,*args, **kwargs):
        cp_id = self.kwargs['pk']
        action = request.GET.get('action')
        cp_obj = ResturantMenuCart.objects.get(id = cp_id)
        cart_obj = cp_obj.cart
          
        if action == 'acr':
             cp_obj.quantity += 1
             cp_obj.subtotal += cp_obj.rate
             cp_obj.save()
             cart_obj.total += cp_obj.rate
             cart_obj.save()
             
        elif action == 'dcr':
             cp_obj.quantity -= 1
             cp_obj.subtotal -= cp_obj.rate
             cp_obj.save()
             cart_obj.total -= cp_obj.rate
             cart_obj.save()
             if cp_obj.quantity == 0:
                 cp_obj.delete()
                 
        elif action == 'rcr':
            cart_obj.total -= cp_obj.subtotal
            cart_obj.save()
            cp_obj.delete()
        else:
            pass
        return redirect('/my-dish/')

class EmptyCartView(RestMixin,View):
    def get(self, request, *args, **kwargs):
        cart_id = request.session.get('cart_id',None)
        if cart_id:
            cart = ResturantCart.objects.get(id=cart_id)
            cart.resturantmenucart_set.all().delete()
            cart.total = 0
            cart.save()
        return redirect('/my-dish/')

class CheckOutView(RestMixin, FormView):
    template_name = "Menu/check_out.html"
    form_class = CheckOutForm
    success_url = reverse_lazy('restu:home')
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.resturantclient:
            pass
        else:
            return redirect("/client-login/?next=/check-out/")
        return super().dispatch(request, *args, **kwargs)
    
    def convert_omr_to_usd(self):
        import requests
        from bs4 import BeautifulSoup
        url = 'https://www.google.com/search?q=omr+to+usd'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find the input element for the target currency (USD)
        target_currency_input = soup.find('input', {'class': 'a61j6'})
        if target_currency_input:
            return float(target_currency_input.get('value'))
        else:
            return 1.0
        
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["resturant"] = Resturant.objects.latest('id')
        context["profile"] = ResturantClient.objects.get(user=self.request.user)
        context["client_id"] = settings.PAYPAL_CLIENT_ID
        cart_id = self.request.session.get('cart_id',None)
        if cart_id:
            cart_obj = ResturantCart.objects.get(id=cart_id)
        else:
            cart_obj = None
        context["cart"] = cart_obj
        context["price_in_usd"] = float(context["cart"].total*self.convert_omr_to_usd())
        return context
    
    def form_valid(self,form):
        cart_id = self.request.session.get('cart_id')
        if cart_id:
            cart_obj = ResturantCart.objects.get(id=cart_id)
            form.instance.user = self.request.user
            form.instance.cart = cart_obj
            form.instance.subtotal = cart_obj.total
            form.instance.total = cart_obj.total
            form.instance.payment_mode = "Paid by PayPal"
            form.instance.payment_id   = self.request.POST.get("payment_id") 
            del self.request.session['cart_id']
            order = form.save()
            return redirect('/')
        else:
            return redirect('restu:home')
        return super().form_valid(form)
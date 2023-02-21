from django.views.generic import TemplateView,FormView,CreateView,UpdateView
from .forms import *
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render,redirect
from resturant.models import * 
from django.urls import reverse_lazy
from django.views import View
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404,redirect,reverse
from django.contrib.auth import authenticate , login ,logout
from django.contrib.auth.views import PasswordChangeView
from .utils import password_reset_token

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
    template_name = 'home.html' 
    form_class =  TableReservasionForm
    success_url = '/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form2']             = ContactForm()
        context["resturant"]         = Resturant.objects.latest('id')
        context["about_resturant"]   = ResturantAboutPlace.objects.latest('id')
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
   
# customer registeration
class ResturantClientRegisterView(CreateView):
    template_name = 'signup.html'
    form_class = ResturantClientRegisterForm
    success_url = '/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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

# customer logout
class ResturantClientLogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('restu:home')

# customer logout
class ResturantClientLoginView(FormView):
    template_name = 'login.html'
    form_class = ResturantClientLoginForm
    success_url = reverse_lazy('restu:home')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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

# customer profile
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

# customer update profile
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

class ForgotPasswordView(FormView):
    template_name = 'forgot_password.html'
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
        return context

class ResetPasswordView(FormView):
    template_name = 'reset_password.html'
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
       
        return context
    
    def form_valid(self,form):
        password = form.cleaned_data['new_password']
        email = self.kwargs.get("email")
        user = User.objects.get(email=email)
        user.set_password(password)
        user.save()
        return super().form_valid(form)

class ChangePasswordView(PasswordChangeView):
    template_name = 'change_password.html'
    success_url = '/'         
    
# add product to my cart
class AddToCartView(RestMixin,TemplateView):
    template_name = "add_to_cart.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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
                cart.save()
        else:
            cart = ResturantCart.objects.create(total=0)
            self.request.session['cart_id'] = cart.id
            cartitem = ResturantMenuCart.objects.create(cart=cart,item=item_obj,
                                                         rate=item_obj.price,quantity=1,
                                                         subtotal=item_obj.price)
            cart.total += item_obj.price
            cart.save()
        return context

# my cart page view
class CartView(RestMixin,TemplateView):
    template_name = "cart.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id = self.request.session.get('cart_id',None)
        if cart_id:
            cart = ResturantCart.objects.get(id=cart_id)
        else:
            cart = None
        context["cart"] = cart 
        return context

# manage in items that are in cart 
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
        return redirect('/my-cart/')

# empty the cart form orders 
class EmptyCartView(RestMixin,View):
    def get(self, request, *args, **kwargs):
        cart_id = request.session.get('cart_id',None)
        if cart_id:
            cart = ResturantCart.objects.get(id=cart_id)
            cart.resturantmenucart_set.all().delete()
            cart.total = 0
            cart.save()
        return redirect('/my-cart/')
    
# check out page view
class CheckOutView(RestMixin, FormView):
    template_name = "check_out.html"
    form_class = CheckOutForm
    success_url = reverse_lazy('restu:home')
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.resturantclient:
            pass
        else:
            return redirect("/client-login/?next=/check-out/")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = ResturantClient.objects.get(user=self.request.user)
        context["client_id"] = settings.PAYPAL_CLIENT_ID
        cart_id = self.request.session.get('cart_id',None)
        if cart_id:
            cart_obj = ResturantCart.objects.get(id=cart_id)
        else:
            cart_obj = None
        context["cart"] = cart_obj
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
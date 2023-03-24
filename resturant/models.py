#--------------------------------------------------------
#    Importing Libraries and using py files in project
#--------------------------------------------------------

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Resturant Table in database
class Resturant(models.Model):
    title_en            = models.CharField(_('Resturant english title'),max_length=255)
    description_en      = models.TextField(_('Resturant english description'))
    opening_sentence_en = models.CharField(_('opening sentence english title'),max_length=255)
    address_en          = models.CharField(_('Resturant english address'),max_length=255)
    phone_num           = models.CharField(_('phone number'),max_length=15)
    logo                = models.ImageField(_('logo Image'),upload_to='resturant/logo/',null=True)
    demo_url            = models.URLField(_('demo url'),null=True)
    email_address       = models.EmailField(_('Resturant Email Address'))
    
    facebook_url        = models.URLField(_('facebook url'),null=True)
    twitter_url         = models.URLField(_('twitter url'),null=True)
    instgram_url        = models.URLField(_('instgram url'),null=True)
    youtube_url         = models.URLField(_('youtube url'),null=True)
    
    title_ar            = models.CharField(_('Resturant arabic title'),max_length=255)
    description_ar      = models.TextField(_('Resturant arabic description'))
    opening_sentence_ar = models.CharField(_('opening sentence arabic title'),max_length=255)
    address_ar          = models.CharField(_('Resturant arabic address'),max_length=255)
    
    class Meta:
        verbose_name_plural = _('Resturant')
    def __str__(self):
        return self.title_en

# ResturantAdmins Table in database
class ResturantAdmins(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,verbose_name=_('username'))
    full_name = models.CharField(_('full name'),max_length=100)
    mobile = models.CharField(_('phone number'),max_length=20)
    class Meta:
            verbose_name_plural = _('Resturant Admins')
    def __str__(self):
        return f"Resturant Admin : {self.user.username}"

# ResturantSiteImages Table in database
class ResturantSiteImages(models.Model):
    image = models.ImageField(_('Resturant Site Images'),upload_to='resturant/site_images/')
    class Meta:
        verbose_name_plural = _('Resturant Site Images')  
    def __str__(self):
        return f"Site Image : {self.id}"

# ResturantGalaryImages Table in database
class ResturantGalaryImages(models.Model):
    image = models.ImageField(_('Resturant Galary Images'),upload_to='resturant/galary_images/')
    class Meta:
        verbose_name_plural = _('Resturant Galary Images')  
    def __str__(self):
        return f"Galary Image : {self.id}"

# ResturantChifs Table in database
class ResturantChifs(models.Model):
    chif_name_en       = models.CharField(_("chif english name"),max_length=200)
    chif_proffesion_en = models.CharField(_("chif english proffesion"),max_length=200)
    chif_profile       = models.ImageField(_("chif profile"),upload_to='resturant/chef_profile/',null=True, blank=True)
    facebook_url       = models.URLField(_('facebook url'),null=True)
    twitter_url        = models.URLField(_('twitter url'),null=True)
    instgram_url       = models.URLField(_('instgram url'),null=True)
    linkedin_url       = models.URLField(_('linkedIn url'),null=True)
    
    chif_name_ar       = models.CharField(_("chif arabic name"),max_length=200)
    chif_proffesion_ar = models.CharField(_("chif arabic proffesion"),max_length=200)
    
    class Meta:
        verbose_name_plural = _('Resturant Chifs')
    def __str__(self):
        return self.chif_name_en

# ResturantTestimonials Table in database
class ResturantTestimonials(models.Model):
    name_en         = models.CharField(_("english name"),max_length=200)
    proffesion_en   = models.CharField(_("english proffesion"),max_length=200)
    profile         = models.ImageField(_("profile"),upload_to='resturant/testimonials/',null=True, blank=True)
    quote_en        = models.TextField(_('english quote'))
    name_ar         = models.CharField(_("arabic name"),max_length=200)
    proffesion_ar   = models.CharField(_("arabic proffesion"),max_length=200)
    quote_ar        = models.TextField(_('arabic quote'))
    class Meta:
        verbose_name_plural = _('ResturantTestimonials')
    
    def __str__(self):
        return self.name_en

# ResturantClient Table in database    
class ResturantClient(models.Model):
    user      = models.OneToOneField(User,verbose_name=_("client"), on_delete=models.CASCADE)
    full_name = models.CharField(_("full_name"),max_length=200)
    address   = models.CharField(_("address"),max_length=200, null=True, blank=True)
    image     = models.ImageField(_("image"),upload_to='resturant_client/',null=True, blank=True)
    phone     = models.CharField(_("phone"),max_length=15)
    join_on   = models.DateTimeField(_("join_on"),auto_now_add=True)
    class Meta:
        verbose_name_plural = _("Resturant Client")
        
    def __str__(self):
        return self.full_name

# ResturantTableReservasion Table in database
class ResturantTableReservasion(models.Model):
    full_name        = models.CharField(_("Full Name"), max_length=255)
    email_address    = models.EmailField(_("Email Adress"))
    phone_number     = models.CharField(_("Phone Number"), max_length=20)
    date             = models.CharField(_('Date'), max_length=10)
    time             = models.CharField(_("Time"), max_length=10)
    number_of_people = models.PositiveIntegerField(_('Number of people'))
    message          = models.TextField(_('Message'))
    confirm          = models.BooleanField(_('Confirm'), default=False)
    class Meta:
        verbose_name_plural = _('Resturant Table Reservasion')
    
    def __str__(self):
        return f"Table Reseved By : {self.full_name}"

# ResturantEvents Table in database
class ResturantEvents(models.Model):
    title_en        = models.CharField(_('Resturant event english title'),max_length=255)
    description_en  = models.TextField(_('Resturant event english description'))
    title_ar        = models.CharField(_('Resturant event arabic title'),max_length=255)
    description_ar  = models.TextField(_('Resturant event arabic description'))
    image           = models.ImageField(_("event image"),upload_to='resturant/events/',null=True, blank=True)
    price           = models.DecimalField(_('Resturant event price'),max_digits=5,decimal_places=2)
    class Meta:
        verbose_name_plural = _('Resturant Events')
    def __str__(self):
        return self.title_en

# ResturantSpecials Table in database
class ResturantSpecials(models.Model):
    category_en     = models.CharField(_('Resturant special english category'),max_length=255)
    title_en        = models.CharField(_('Resturant special english title'),max_length=255)
    description_en  = models.TextField(_('Resturant special english description'))
    image           = models.ImageField(_("image"),upload_to='resturant/specials/',null=True, blank=True)
    category_ar     = models.CharField(_('Resturant special arabic category'),max_length=255)
    title_ar        = models.CharField(_('Resturant special arabic title'),max_length=255)
    description_ar  = models.TextField(_('Resturant special arabic description'))
    class Meta:
            verbose_name_plural = _('Resturant Specials')
    def __str__(self):
        return self.category_en

# ResturantWhyUs Table in database
class ResturantWhyUs(models.Model):
    title_en        = models.CharField(_('Resturant WhyUs english title'),max_length=255)
    description_en  = models.CharField(_('Resturant WhyUs english description'),max_length=255)
    title_ar        = models.CharField(_('Resturant WhyUs arabic title'),max_length=255)
    description_ar  = models.CharField(_('Resturant WhyUs arabic description'),max_length=255)
    class Meta:
            verbose_name_plural = _('Resturant WhyUs')
    def __str__(self):
        return self.title_en

# ResturantAboutPlace Table in database    
class ResturantAboutPlace(models.Model):
    title_en        = models.CharField(_('Resturant About Place english title'),max_length=255)
    description_en  = models.TextField(_('Resturant About Place english description'))
    title_ar        = models.CharField(_('Resturant About Place arabic title'),max_length=255)
    description_ar  = models.TextField(_('Resturant About Place arabic description'))
    image           = models.ImageField(_("About Place image"),upload_to='resturant/place/',null=True, blank=True)
    class Meta:
        verbose_name_plural = _('Resturant About Place')
    def __str__(self):
        return self.title_en

# ResturantMenuCategory Table in database
class ResturantMenuCategory(models.Model):
    title_en = models.CharField(_('menu category english title'),max_length=255)
    title_ar = models.CharField(_('menu category arabic title'),max_length=255)
    class Meta:
        verbose_name_plural = _('Resturant Menu Category')
        
    def __str__(self):
        return self.title_en

# ResturantMenu Table in database
class ResturantMenu(models.Model):
    category        = models.ForeignKey(ResturantMenuCategory,on_delete=models.CASCADE,verbose_name=_('menu category'))
    title_en        = models.CharField(_('menu item english title'),max_length=255)
    description_en  = models.TextField(_('menu item english description'))
    title_ar        = models.CharField(_('menu item arabic title'),max_length=255)
    description_ar  = models.TextField(_('menu item arabic description'))
    price           = models.DecimalField(_('menu item price'),max_digits=6,decimal_places=3)
    image           = models.ImageField(_('menu item image'),upload_to='menu-item/images/',null=True, blank=True)
    class Meta:
        verbose_name_plural = _('Resturant Menu')
    def __str__(self):
        return self.title_en

# ResturantCart Table in database
class ResturantCart(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE, blank = True, null=True,verbose_name=_('client'))
    total = models.DecimalField(_('total'),max_digits=6,decimal_places=3,default=0.0)
    created_at = models.DateTimeField(_('created at'),auto_now_add=True)
    class Meta:
        verbose_name_plural=_('Resturant Cart')
    def __str__ (self):
        return "Cart : " + str(self.id)

# ResturantMenuCart Table in database
class ResturantMenuCart(models.Model):
    cart = models.ForeignKey(ResturantCart,on_delete=models.CASCADE,verbose_name=_('cart'))
    item = models.ForeignKey(ResturantMenu , on_delete = models.CASCADE,verbose_name=_('item'))
    rate = models.DecimalField(_('rate'),max_digits=6,decimal_places=3,default=0.0)            
    quantity = models.PositiveIntegerField(_('quantity'),default=1)
    subtotal = models.DecimalField(_('subtotal'),max_digits=6,decimal_places=3,default=0.0) 
    class Meta:
        verbose_name_plural = _('Resturant Menu Cart')
    def __str__ (self):
        return "Cart : " + str(self.cart.id) +" ResturantMenuCart : "+ str(self.id)

# ResturantMenuOrder Table in database
class ResturantMenuOrder(models.Model):
    # order status
    ORDER_STATUS = (
        (_("Order Received"),_("Order Received")),
        (_("Order Processing"),_("Order Processing")),
        (_("Order On The Way"),_("Order On The Way")),
        (_("Order Completed"),_("Order Completed")),
        (_("Order Canceled"),_("Order Canceled")),
        )

    cart = models.OneToOneField(ResturantCart,on_delete=models.CASCADE,verbose_name=_('cart'))
    user = models.ForeignKey(User,on_delete = models.SET_NULL, blank = True, null=True,verbose_name=_('client'))
    first_name = models.CharField(_('first name'),max_length=200,null=True) 
    last_name = models.CharField(_('last name'),max_length=200,null=True) 
    phone_num = models.CharField(_('phone number'),max_length=15)
    email = models.EmailField(_('email address'),null=True , blank = True)
    subtotal = models.DecimalField(_('subtotal'),max_digits=6,decimal_places=3)
    total = models.DecimalField(_('total'),default=0.000,max_digits=6,decimal_places=3)
    order_status = models.CharField(_('order status'),max_length=50,choices = ORDER_STATUS,default=_("Order Received"))
    created_at = models.DateTimeField(_('created at'),auto_now_add = True)
    payment_mode = models.CharField(_('payment mode'),max_length=200,null=True)  
    payment_id = models.CharField(_('payment id'),max_length=200,null=True) 
    def save(self,*args,**kwargs):
        self.first_name = self.first_name.lower()
        return super(ResturantMenuOrder,self).save(*args,**kwargs)
    class Meta:
        verbose_name_plural = _('Resturant Menu Order')
    def __str__(self):
        return "Order : "+ str(self.id)
from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User

from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey

# Create your models here.
class Settings(models.Model):
    # general settings
    address = models.CharField(max_length=300, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    facebook = models.CharField(max_length=300, blank=True, null=True)
    twitter = models.CharField(max_length=300, blank=True, null=True)
    instagram = models.CharField(max_length=300, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    video = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.email

class Category(MPTTModel):
    parent = TreeForeignKey('self',blank=True, null=True ,related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=300, blank=True, null=True)
    slug = models.SlugField()
    icon = models.CharField(max_length=20, blank=True, null=True)
    image = models.ImageField(upload_to='category/',)
    style_tabs = models.CharField(max_length=10,blank=True, null=True)
    style_delay = models.CharField(max_length=4, blank=True, null=True)
    active = models.CharField(max_length=50, blank=True, null=True)
    show = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):                           # __str__ method elaborated later in
        full_path = [self.title]                  # post.  use __unicode__ in place of
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' / '.join(full_path[::-1])


    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50" width="50"/>'.format(self.image.url))
        else:
            return ""

class Product(models.Model):

    STATUS = (
        ('New', 'New'),
        ('Sale', 'Sale'),
        ('None', 'None'),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, blank=True, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    discount_price = models.DecimalField(max_digits=7, decimal_places=2,  blank=True, null=True)
    image = models.ImageField(upload_to='product/')
    fullimage = models.ImageField(upload_to='product/', blank=True, null=True)
    slug = models.SlugField()
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50" width="50"/>'.format(self.image.url))
        else:
            return ""


class Slideshow(models.Model):
    image = models.ImageField(upload_to='slideshow/')
    headings = models.CharField(max_length=200, blank=True, null=True)
    desc = models.CharField(max_length=400, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.headings

class Gallery(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    desc = models.CharField(max_length=300, blank=True, null=True)
    img = models.ImageField(upload_to='gallery/')
    col_xs = models.CharField(max_length=4, blank=True, null=True)
    col_sm = models.CharField(max_length=4, blank=True, null=True)
    col_xl = models.CharField(max_length=4, blank=True, null=True)
    size_style = models.CharField(max_length=20, blank=True, null=True)
    slide_style = models.CharField(max_length=20, blank=True, null=True)
    height = models.CharField(max_length=4, blank=True, null=True)
    width = models.CharField(max_length=4, blank=True, null=True)
    
    def __str__(self):
        return self.title

    def image_tag(self):
        if self.img.url is not None:
            return mark_safe('<img src="{}" height="50" width="50"/>'.format(self.img.url))
        else:
            return ""

class Image(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery/images')
    gallery = models.ForeignKey(Gallery, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class Bookings(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    service = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name

class NewsLetter(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email


class AboutUs(models.Model):
    topic = models.CharField(max_length=50)
    sub_topic = models.CharField(max_length=100)
    details = models.TextField()
    image = models.ImageField(upload_to='about_us/')
    style_tabs = models.CharField(max_length=10,blank=True, null=True)
    style_delay = models.CharField(max_length=4, blank=True, null=True)
    active = models.CharField(max_length=50, blank=True, null=True)
    show = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.topic
        
    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50" width="50"/>'.format(self.image.url))
        else:
            return ""

class Team(models.Model):
    name = models.CharField(max_length=50)
    post = models.CharField(max_length=50)
    image = models.ImageField(upload_to='team/')
    delay = models.CharField(max_length=2, blank=True, null=True)
    facebook = models.CharField(max_length=300, blank=True, null=True)
    twitter = models.CharField(max_length=300, blank=True, null=True)
    instagram = models.CharField(max_length=300, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name

    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50" width="50"/>'.format(self.image.url))
        else:
            return ""


class History(models.Model):
    title = models.CharField(max_length=50)
    detail = models.CharField(max_length=400)
    year = models.IntegerField(blank=True, null=True)
    style_tabs = models.CharField(max_length=10,blank=True, null=True)
    active = models.CharField(max_length=50, blank=True, null=True)
    show = models.CharField(max_length=50, blank=True, null=True)


    def __str__(self):
        return self.title


class IconClassic(models.Model):
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=200)
    delay = models.CharField(max_length=2)
    icon = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True, null=True)
    image = models.ImageField(blank=True, upload_to='images/users/', null=True)

    def __str__(self):
        return self.user.username


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.product.title

    def amount(self):
        if self.product.discount_price:
            calc = self.product.discount_price * self.quantity
        else:
            calc = self.product.price * self.quantity
        return calc


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ManyToManyField(Cart)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def total(self):
        total = 0
        for val in self.cart.all():
            total += val.amount()
        return total
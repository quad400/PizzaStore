from django.shortcuts import render,get_object_or_404
from django.contrib import messages
from django.http.response import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from django.conf import settings

import stripe
from allauth.account.views import LoginView,SignupView,LogoutView
from .models import (
            Slideshow, 
            Category, 
            Product, 
            Gallery, 
            Bookings, 
            NewsLetter,Settings, 
            AboutUs, Team, 
            History, IconClassic,
            UserProfile,Comment,
            Cart,Order
)
from .forms import (
                BookingForm, NewsLetterForm, 
                UserProfileForm, UserUpdate,
                CommentForm
                )


# Create your views here.
def homepage(request):
    slide = Slideshow.objects.all()
    category = Category.objects.all()
    products = Product.objects.filter(status='New')
    product_cta = Product.objects.all().order_by('?')[1]
    galleries = Gallery.objects.all()
    settings = Settings.objects.all()
    comments = Comment.objects.all()
    context = {
        'slide': slide,
        'settings': settings,
        'category': category,
        'products': products,
        'product_cta': product_cta,
        'galleries': galleries,
        'comments': comments,
        
    }
    return render(request, 'product/homepage.html', context)


def bookings(request):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            data = Bookings()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.message = form.cleaned_data['message']
            data.service = form.cleaned_data['service']
            data.save()
            messages.success(request, 'You have successfully book an event. Thank You')
            return HttpResponseRedirect(url)

        messages.error(request, 'Invalid input')
        return HttpResponseRedirect(url)

def index(request):
    category = Category.objects.all()
    settings = Settings.objects.all()
    context = {
        'category': category,
        'settings': settings,
    }
    return render(request, 'constant/base.html', context)


def newsletter(request):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            data = NewsLetter()
            data.email = form.cleaned_data['email']
            data.save()
            messages.success(request, 'You have successfully book an event. Thank You')
            return HttpResponseRedirect(url)
        messages.error(request, 'Invalid input')
        return HttpResponseRedirect(url)


def about_us(request):
    category = Category.objects.all()
    settings = Settings.objects.all()
    about_us = AboutUs.objects.all()
    teams = Team.objects.all()
    history = History.objects.all()
    icons = IconClassic.objects.all()

    context = {
        'settings': settings,
        'category': category,
        'about_us': about_us,
        'teams': teams,
        'history': history,
        'icons': icons,
    }
    return render(request, 'others/aboutus.html', context)


def account(request):
    settings = Settings.objects.all()
    category = Category.objects.all()
    context = {
        'category': category,
        'settings': settings,
    }
    return render(request, 'account/account_detail.html', context)


class MyLoginView(LoginView):

    def get_context_data(self, **kwargs):
        context = super(MyLoginView, self).get_context_data(**kwargs)
        settings = Settings.objects.all()
        category = Category.objects.all()
        context.update({
        'category': category,
        'settings': settings
        })
        return context


class MySignUpView(SignupView):
    
    def get_context_data(self, **kwargs):
        context = super(MySignUpView, self).get_context_data(**kwargs)
        settings = Settings.objects.all()
        category = Category.objects.all()
        context.update({
        'category': category,
        'settings': settings
        })
        return context

class MyLogout(LogoutView):

    def get_context_data(self, **kwargs):
        context = super(MyLogout, self).get_context_data(**kwargs)
        settings = Settings.objects.all()
        category = Category.objects.all()
        context.update({
        'category': category,
        'settings': settings
        })
        return context


@login_required
def account_detail(request):
    profile_qs = UserProfile.objects.filter(user=request.user)
    settings = Settings.objects.all()
    category = Category.objects.all()

    if profile_qs.exists():
        profile = UserProfile.objects.get(user=request.user)
        context = {
                'profile': profile,
                'category': category,
                'settings': settings
            }
        return render(request, 'account/account_detail.html', context)

    else:
        profile = UserProfile.objects.create(user=request.user)
        context = {
                    'profile': profile,
                    'category': category,
                    'settings': settings
                }
        return render(request, 'account/account_detail.html', context)


@login_required
def account_update(request):
    settings = Settings.objects.all()
    category = Category.objects.all()
    if request.method == 'POST':
        user_info = UserUpdate(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_info.is_valid() and profile_form.is_valid():
            user_info.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated')
            return HttpResponseRedirect('account/account_detail.html')
        
        messages.success(request, 'Invalid input')
        return HttpResponseRedirect('account/account_detail.html')
 
    else:
        user_info = UserUpdate(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.userprofile) #"userprofile" model -> OneToOneField relatinon with user
        context = {
            'user_info': user_info,
            'profile_form': profile_form,
            'category': category,
            'settings': settings
        }
        return render(request, 'account/account_update.html', context)


def contact_us(request):

    settings = Settings.objects.all()
    category = Category.objects.all()
    context = {
                    'category': category,
                    'settings': settings
                }
    return render(request, 'others/contactus.html', context)


def comment(request):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = Comment()
            data.user_id = request.user.id
            data.subject = form.cleaned_data['subject']
            data.comment = form.cleaned_data['comment']

            data.save()
            messages.success(request, 'You have successfully add your comment. Thank You')
            return HttpResponseRedirect('/')

        messages.error(request, 'Invalid input')
        return HttpResponseRedirect(url)


def menu(request, slug):
    category = Category.objects._mptt_filter(slug=slug)
    products = Product.objects.filter(category__slug=slug)
    categories =  Category.objects.all()
    settings = Settings.objects.all()

    context = {
        'category': category,
        'settings': settings,
        'categories': categories,
        'products': products,
    }
    return render(request, 'product/menu_page.html', context)


@login_required
def cart(request):
    settings = Settings.objects.all()
    category = Category.objects.all()
    carts = Cart.objects.filter(user=request.user)
    # order = Order.objects.get(user=request.user)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]

        if order.ordered == True and carts.ordered == True:
            order.cart.remove(carts)
            order.cart.delete()
        
        context = {
                        'category': category,
                        'settings': settings,
                        'carts': carts,
                        'order': order,
                    }
    else:
        context = {
                'category': category,
                'settings': settings,
            }
    return render(request, 'others/cart.html', context)


@login_required
def add_to_cart(request, slug):
    url = request.META.get('HTTP_REFERER')
    product = get_object_or_404(Product, slug=slug)
    cart, created = Cart.objects.get_or_create(
        product=product,
        user=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
        )
    if order_qs.exists():
        order = order_qs[0]
        if order.cart.filter(product__slug=product.slug).exists():
            cart.quantity += 1
            cart.save()
            messages.success(request, "Item was successfully updated")
            return HttpResponseRedirect(url)
        else:
            order.cart.add(cart)
            messages.success(request, "Item was successfully added to cart")
            return HttpResponseRedirect(url)

    else:
        order = Order.objects.create(
            user=request.user
        )
        order.cart.add(cart)
        messages.success(request, "Item was successfully added to cart")
        return HttpResponseRedirect(url)


@login_required
def remove_product_quantity(request,slug):
    url = request.META.get('HTTP_REFERER')
    product = get_object_or_404(Product, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.cart.filter(product__slug=product.slug).exists():
            cart = Cart.objects.filter(
                product=product, user=request.user, ordered=False
            )[0]
            if cart.quantity > 1:
                cart.quantity -= 1
                cart.save()
            else:
                order.cart.remove(cart)
                cart.delete()
            messages.info(request, "This item quantity was updated.")
            return HttpResponseRedirect(url)
        else:
            messages.info(request, "This item was not in your cart")
            return HttpResponseRedirect(url)
    else:
        messages.info(request, "You do not have an active order")
        return HttpResponseRedirect(url)


@login_required
def remove_product(request, slug):
    url = request.META.get('HTTP_REFERER')
    product = get_object_or_404(Product, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.cart.filter(product__slug=product.slug).exists():
            cart = Cart.objects.filter(
                product=product, user=request.user, ordered=False
            )[0]
            order.cart.remove(cart)
            cart.delete()
            messages.info(request, "This item was removed from your cart.")
            return HttpResponseRedirect(url)
        messages.info(request, "This item was not in your cart")
        return HttpResponseRedirect(url)
    messages.info(request, "You do not have an active order")
    return HttpResponseRedirect(url)


def checkout(request):
    category =  Category.objects.all()
    settings = Settings.objects.all()
    context = {
        'category': category,
        'settings': settings,
    }
    return render(request, 'others/checkout.html', context)


@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(
            stripe_config, safe=False
        )


@csrf_exempt
def create_checkout_session(request):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'GET':
        domain_url = 'http://localhost:8000/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        order_qs = Order.objects.filter(user=request.user)
        if order_qs.exists():
            order = order_qs[0]
            try:
                checkout_session = stripe.checkout.Session.create(
                    success_url = domain_url + 'success',
                    cancel_url = domain_url + 'cancelled',
                    payment_method_types = ['card'],
                    mode = 'payment',
                    line_items = [
                        {
                            "price_data": {
                                "currency": "usd",
                                "unit_amount_decimal": order.total() * 100,
                                "product_data": {
                                    "name": "Good Boy",
                                }
                            },
                            "quantity": 1,
                        },
                    ] 
                ) 
                order.ordered = True
                order.save()
                return JsonResponse({'sessionId': checkout_session['id']})
            except Exception as e:
                return JsonResponse({'error': str(e)})

        else:
            messages.info(request, "You have no product in your cart")
            return HttpResponseRedirect(url)

def success(request):
    category =  Category.objects.all()
    settings = Settings.objects.all()

    context = {
        'category': category,
        'settings': settings,
    }
    return render(request, 'others/success.html', context)


def cancelled(request):
    category =  Category.objects.all()
    settings = Settings.objects.all()

    context = {
        'category': category,
        'settings': settings,
    }
    return render(request, 'others/cancelled.html', context)


@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    endpoint_secret = settings.STRIPE_WEBHOOK_KEY
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # invalid signature
        HttpResponse(status=400)
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        print(session)
    return HttpResponse(status=200)
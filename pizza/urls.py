from django.urls import path

from .views import (
            index, bookings, 
            newsletter,homepage,
            about_us,account_detail, account_update,
            MyLoginView, MySignUpView,checkout,
            MyLogout,contact_us,comment, menu,cart,
            add_to_cart, remove_product, remove_product_quantity, 
            stripe_config, create_checkout_session,success,cancelled,
            stripe_webhook
        )
urlpatterns = [
    path('index', index, name='index'),
    path('', homepage, name='homepage'),
    path('booking', bookings, name='booking'),
    path('newsletter', newsletter, name='newsletter'),

    # other
    path('aboutus', about_us, name='aboutus'),
    path('contact_us', contact_us, name='contact_us'),
    path('comment', comment, name='comment'),
    path('cart', cart, name='cart'),
    path('checkout', checkout, name='checkout'),
    path('add_to_cart/<slug:slug>', add_to_cart, name='add_to_cart'),
    path('remove_product/<slug:slug>', remove_product, name='remove_product'),
    path('remove_product_quantity/<slug:slug>', remove_product_quantity, name='remove_product_quantity'),

    # account
    path('account_detail', account_detail, name='account_detail'),
    path('accounts/login', MyLoginView.as_view(), name='account_login'),
    path('accounts/signup', MySignUpView.as_view(), name='account_signup'),
    path('accounts/logout', MyLogout.as_view(), name='account_logout'),
    path('account_update', account_update, name='account_update'),

    # product
    path('menu/<slug:slug>', menu, name='menu' ),

    path('config', stripe_config),
    path('create-checkout-session', create_checkout_session),
    path('success', success),
    path('cancelled', cancelled),
    path('webhooks/stripe',stripe_webhook, name='stripe_webhook')
]
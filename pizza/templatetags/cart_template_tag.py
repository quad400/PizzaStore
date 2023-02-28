from django.template import Library

from pizza.models import Order
register = Library()

@register.filter()
def cart_tags(user):
    if user.is_authenticated:
        qs = Order.objects.filter(user=user, ordered=False)
        if qs.exists():
            return qs[0].cart.count()
    return 0
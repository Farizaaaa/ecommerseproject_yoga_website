from cart.models import Cart, CartItem
from . views import _cart_id,add_cart,cart_detail
def counter(request):
    item_count=0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.filter(cart_id=_cart_id(request))
            cart_item=CartItem.objects.all().filter(cart=cart[:1])
            for cart_item in cart_item:
                item_count += cart_item.quantity
        except Cart.DoesNotExist:
            Item_count=0
    return dict(item_count=item_count)

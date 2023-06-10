from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from cart.models import Cart, CartItem
from ecommerce.models import product
# Create your views here.
def fun(request):
    return render(request,'Product.html')
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart=request.session.create()
    return cart
def add_cart(request,product_id):

    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_cart_id(request))
        cart.save()
    try:
        productss = product.objects.get(id=product_id)
        cart_item=CartItem.objects.get(product=productss,cart=cart)
        if cart_item.quantity < cart_item.product.stock:
           cart_item.quantity += 1
        cart_item.save()

    except CartItem.DoesNotExist:
        productss = product.objects.get(id=product_id)
        cart_item=CartItem.objects.create(product=productss,quantity=1,cart=cart)
        cart_item.save()
    return redirect('cart:cart_detail')
def cart_detail(request,total=0,counter=0,cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items=CartItem.objects.filter(cart=cart,active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',dict(cart_items=cart_items,total=total,counter=counter))
    
def cart_remove(request,product_id):
    cart=Cart.objects.get(cart_id=_cart_id(request))
    products=get_object_or_404(product,id=product_id)
    cart_item=CartItem.objects.get(product=products,cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart:cart_detail')
def full_remove(request,product_id):
    cart=Cart.objects.get(cart_id=_cart_id(request))
    products=get_object_or_404(product,id=product_id)
    cart_item=CartItem.objects.get(product=products,cart=cart)
    cart_item.delete()
    return redirect('cart:cart_detail')
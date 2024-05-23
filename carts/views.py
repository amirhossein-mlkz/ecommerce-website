from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from django.http import HttpRequest
from .models import Cart, CartItem
from store.models import Product

def __get_cart_id(request:HttpRequest):
    """returns session id as cart id

    Args:
        request (_type_): _description_
    """
    
    cart_id = request.session.session_key
    if not cart_id:
        cart_id = request.session.create()
    return cart_id



def add_to_cart(request:HttpRequest, product_id):
    cart_id = __get_cart_id(request)
    try:
        cart = Cart.objects.get(cart_id=cart_id)
    except Cart.DoesNotExist:
        cart= Cart.objects.create(
                    cart_id=cart_id
                    )
        cart.save()

    product = Product.objects.get(id=product_id)
    
    try:
        cart_item = CartItem.objects.get(product=product, 
                                         cart=cart)
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(product=product,
                                            cart=cart,
                                            quantity=1)
        cart_item.save()
    return redirect('cart')

def change_quanity(request:HttpRequest, item_id, state):
    
    item = CartItem.objects.get(id=item_id)
    if state=='up':
        item.quantity = item.quantity + 1
        item.save()
    elif state=='down':
        item.quantity = item.quantity - 1
        item.save()
    
    elif state=='remove':
        item.delete()

    return redirect('cart')
    


def cart(request:HttpRequest):
    template = get_template('cart.html')
    total_price = 0
    try :
        cart = Cart.objects.get(cart_id=__get_cart_id(request))
        cart_items= CartItem.objects.filter(cart=cart, is_active=True)
        for item in cart_items:
            total_price = total_price + item.product.price * item.quantity

    except:
        cart_items = []
    print(total_price)
    context = {
        'cart_items':cart_items,
        'total_price':total_price
    }
    return HttpResponse(template.render(context=context, request= request))
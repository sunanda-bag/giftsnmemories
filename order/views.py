from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.views import generic
from .models import *
from product.models import *

from .forms import *
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required()
def addBox(request):
    
    if request.method=='POST':
        box_id = request.POST.get('box-id')
        box_var = GiftBox.objects.filter(id=box_id)[0]
        print('box_var',box_var)
        #check if any box item already present, if present remove and create new
        giftbox_qs = GiftBoxItem.objects.filter(user=request.user, added2cart_status=False)
        # if giftbox_qs.exists():
        #     giftbox= giftbox_qs[0]
        #     if giftbox.box_type.filter(user=request.user, gift_box=box_var).exists():
        #         box_item = giftbox.box_type.filter(user=request.user)[0]
        #         box_item.delete()
        #         box_item = BoxType.objects.create(user=request.user, gift_box=box_var)
        #         giftbox.box_type.add(box_item)
        #         # box_item.save()  
        #         # print(box_item)
        #     else:
        #         box_item = BoxType.objects.create(user=request.user, gift_box=box_var)
        #         giftbox.box_type.add(box_item)
        # else:
        #     giftbox = GiftBoxItem.objects.create(user=request.user)
        #     box_item = BoxType.objects.create(user=request.user, gift_box=box_var)
        #     giftbox.box_type.add(box_item)
       
        #     return HttpResponseRedirect(reverse('product:build-a-box'))
        return HttpResponseRedirect(reverse('product:build-a-box'))

@login_required()
def addCard(request):
    if request.method=='POST':
        card_id = request.POST.get('card-id')
        card_var = Card.objects.get(id=card_id)

        #check if any card item already present, if present remove and create new
        try:
            card_type = CardType.objects.get(user=request.user,card=card_var)
            
            if card_type:
                print(card_type)
            #     card_type.delete()
            #     card_type = CardType.objects.get(user=request.user, card=card_var)
            #     card_type.save()
        except:
            CardType.objects.create(user=request.user, card=card_var)
        finally:
            return HttpResponseRedirect(reverse('product:build-a-box'))


@login_required()
def deleteCard(request):
    if request.method=='POST':
        card_id = request.POST.get('card-id')
        card = CardType.objects.get(id=card_id)
        card.delete()
        return HttpResponseRedirect(reverse('product:build-a-box'))
            

@login_required()
def addGiftToBox(request):
    if request.method=='POST':
        product_var_id = request.POST.get('product-id')
        product_var = ProductVariation.objects.get(id=product_var_id)
        print(product_var)
        #check if the gift product item already present, if present add one quantity else create new
        try:
            gift_item = GiftItem.objects.get(user=request.user, product=product_var)
            print(gift_item)
            if gift_item:
                gift_item.quantity += 1
                gift_item.save()
        except:
            GiftItem.objects.create(user=request.user, product=product_var)
        finally:
            return HttpResponseRedirect(reverse('product:build-a-box'))


@login_required()
def AddCardMessage(request):
    if request.method=='POST':
        card_var_id = request.POST.get('card-id')
        card_var = Card.objects.get(id=card_var_id)

        recipient= request.POST.get('recipient')
        sender= request.POST.get('sender')
        front_content= request.POST.get('fc_content')
        back_content= request.POST.get('bc_content')
        CardMessage.objects.create(card=card_var, recipient=recipient,sender=sender,card_content_front=front_content,card_content_back=back_content)
    return HttpResponseRedirect(reverse('product:build-a-box'), {'card_message_form': CardMessageForm,})
    # return HttpResponseRedirect(reverse('product:build-a-box'))
    

@login_required()
def deleteFromGiftBox(request):
    if request.method=='POST':
        item_id = request.POST.get('item-id')
        item = OrderItem.objects.get(id=item_id)
        item.delete()
        return HttpResponseRedirect(reverse('order:cart'))

@login_required()
def addToWishlist(request):
    if request.method=='POST':
        product_var_id = request.POST.get('product-id')
        product_var = ProductVariation.objects.get(id=product_var_id)

        #check if the wishlist item already present, if present add one quantity else create new
        try:
            wish_item = WishItem.objects.get(user=request.user, product=product_var)
            print(wish_item)
            if wish_item:
                wish_item.quantity += 1
                wish_item.save()
        except:
            WishItem.objects.create(user=request.user, product=product_var)
        finally:
            return HttpResponseRedirect(reverse('order:wishlist'))

@login_required()
def deleteFromWishlist(request):
    if request.method=='POST':
        item_id = request.POST.get('item-id')
        WishItem.objects.filter(id=item_id).delete()
        return HttpResponseRedirect(reverse('order:wishlist'))

@login_required()
def addToCart(request):
    if request.method=='POST':
        product_var_id = request.POST.get('product-id')
        product_var = ProductVariation.objects.get(id=product_var_id)

        order_qs = Order.objects.filter(user=request.user, ordered=False)
        if order_qs.exists():
            order= order_qs[0]
            if order.items.filter(user=request.user, product=product_var).exists():
                order_item = order.items.get(user=request.user, product=product_var)
                order_item.quantity += 1
                order_item.save()  
                print(order_item)
            else:
                order_item = OrderItem.objects.create(user=request.user, product=product_var)
                order.items.add(order_item)
        else:
            order = Order.objects.create(user=request.user)
            order_item = OrderItem.objects.create(user=request.user, product=product_var)
            order.items.add(order_item)

        try:
            # to remove from wishlist if present in wishlist
            wishlist_item = WishItem.objects.get(user=request.user, product=product_var)
            if wishlist_item:
                wishlist_item.delete()
        finally:
            return HttpResponseRedirect(reverse('order:cart'))

@login_required()
def deleteFromCart(request):
    if request.method=='POST':
        item_id = request.POST.get('item-id')
        item = OrderItem.objects.get(id=item_id)
        item.delete()
        return HttpResponseRedirect(reverse('order:cart'))

@login_required()
def addOneQuantity(request):
    if request.method=='POST':
        item_id = request.POST.get('item-id')
        item = OrderItem.objects.get(id=item_id)
        item.quantity += 1
        item.save()
        return HttpResponseRedirect(reverse('order:cart'))

@login_required()
def deleteOneQuantity(request):
    if request.method=='POST':
        item_id = request.POST.get('item-id')
        item = OrderItem.objects.get(id=item_id)
        if item.quantity == 1:
            item.delete()
        else:
            item.quantity -= 1
            item.save()
        return HttpResponseRedirect(reverse('order:cart'))

class WishlistView(LoginRequiredMixin,generic.View):
    def get(self, *args, **kwargs):
        items = WishItem.objects.filter(user=self.request.user)
        context = {
            'items':items,
        }
        return render(self.request, 'order/wishlist.html', context)

class CartView(LoginRequiredMixin,generic.View):
    def get(self, *args, **kwargs):
        order_qs = Order.objects.filter(user=self.request.user, ordered=False)
        if order_qs.exists():
            order_object = order_qs[0]
        else:
            order_object = Order.objects.create(user=self.request.user)
        context = {
            'order_object':order_object,
        }
        return render(self.request, 'order/cart.html', context)

def orderCheckout(request):
    if request.method=='POST':
        user=request.user
        if user.is_authenticated:
            gift_box_items = GiftBoxItem.objects.all()
            gift_box_items = GiftBoxItem.objects.filter(user=request.user,added2cart_status=False)
            if gift_box_items.exists():
                gift_box_items_qs=gift_box_items[0]
        # order = Order.objects.get(user=request.user, ordered=False)
        # order.name = request.POST.get('name')
        # order.mobile = request.POST.get('mobile')
        # order.email = request.POST.get('email')
        # order.address = request.POST.get('address')
        # order.city = request.POST.get('city')
        # order.pincode = request.POST.get('pincode')
        # order.price = request.POST.get('price')
        # order.quantity = request.POST.get('quantity')
        # order.save()
        # return HttpResponseRedirect(reverse('order:checkout'))
        return render(request, 'order/checkout.html', {'items':gift_box_items_qs})

class CheckoutView(LoginRequiredMixin,generic.View):
    def get(self, *args, **kwargs):
        order_qs = Order.objects.filter(user=self.request.user, ordered=False)
        if order_qs.exists():
            order = order_qs[0]
        else:
            order = Order.objects.create(user=self.request.user)
        context = {
            'order':order,
        }
        return render(self.request, 'order/checkout.html', context)

class ConfirmationView(LoginRequiredMixin,generic.View):
    def get(self, *args, **kwargs):
        return render(self.request, 'order/confirmation.html')


#for payments
import stripe
from django.conf import settings
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import datetime

# stripe.api_key = settings.STRIPE_SECRET_KEY

class CreateCheckoutSessionView(generic.View):
    def post(self, request, *args, **kwargs):
        host = request.get_host()
        
        order_id = request.POST.get('order-id')
        order = Order.objects.get(id=order_id)

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'inr',
                        'unit_amount': order.total_amount()*100,
                        'product_data': {
                            'name': order.id,
                            # 'images': ['https://i.imgur.com/EHyR2nP.png'],
                        },
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url="http://{}{}".format(host,reverse('order:payment-success')),
            cancel_url="http://{}{}".format(host,reverse('order:payment-cancel')),
        )
        # return JsonResponse({
        #     'id':checkout_session.id
        # })
        return redirect(checkout_session.url, code=303)

def paymentSuccess(request):
    context = {
        'payment_status':'success'
    }
    return render(request, 'order/confirmation.html', context)

def paymentCancel(request):
    context = {
        'payment_status':'cancel'
    }
    return render(request, 'order/confirmation.html',context)

#event handler for stripe payments
# endpoint_secret = settings.STRIPE_WEBHOOK_SECRET
@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
    except ValueError:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

        if session.payment_status == "paid":
            # Fulfill the purchase
            line_item = session.list_line_items(session.id, limit=1).data[0]
            order_id = line_item['description']
            fulfill_order(order_id)

    # Passed signature verification
    return HttpResponse(status=200)

def fulfill_order(order_id):
    order = Order.objects.get(id=order_id)
    order.ordered = True
    order.orderDate = datetime.datetime.now()
    order.save()

    for item in order.items.all():
        product_var = ProductVariation.objects.get(id=item.product.id)
        product_var.stock -=  item.quantity
        product_var.save()
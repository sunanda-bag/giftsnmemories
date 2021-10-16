from django.views.generic import View
from django.shortcuts import render
# from product.models import Offer, Deal, ProductVariation
from order.models import *


class IndexView(View):
    def get(self, *args, **kwargs):
        gift_box_items = GiftBoxItem.objects.all()
        context = {
            'gift_box_items':gift_box_items
            # 'offers': Offer.objects.all(),
            # 'mens_products': ProductVariation.objects.filter(product__gender='M').order_by('-id')[:4],
            # 'womens_products': ProductVariation.objects.filter(product__gender='F').order_by('-id')[:4],
            # 'deal': Deal.objects.order_by('-id')[0],
            
        }
        return render(self.request, 'index.html', context)



def about(request):

#     categories = Category.objects.all()
#     context = {'categories': categories}
    context = {}
    return render(request, 'about.html', context)


def contact(request):

#     categories = Category.objects.all()
#     if request.method == 'POST':
#         name = request.POST['name']
#         email = request.POST['email']
#         phone = request.POST['phone']
#         message = request.POST['message']
#         message_body = f'''Hey, I am {name}.My phone number is {phone}.

#         {message}
#         '''
#         # send an email
#         send_mail(
#             f'Message from {name} ',
#             message_body,
#             email,
#             ['testerwebsite007@gmail.com'],
#             fail_silently=False,
#         )
#         context = {'name': name, 'categories': categories}

#     else:
#         context = {'categories': categories}
    context = {}
    return render(request, 'contact.html', context)
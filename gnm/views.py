from django.views.generic import View
from django.shortcuts import render
# from product.models import Offer, Deal, ProductVariation
from order.models import *


class IndexView(View):
    def get(self, *args, **kwargs):
        context = {
            # 'offers': Offer.objects.all(),
            # 'mens_products': ProductVariation.objects.filter(product__gender='M').order_by('-id')[:4],
            # 'womens_products': ProductVariation.objects.filter(product__gender='F').order_by('-id')[:4],
            # 'deal': Deal.objects.order_by('-id')[0],
            
        }
        return render(self.request, 'index.html', context)
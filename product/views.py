from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, View
from django.utils.text import slugify
from order.models import *

from .models import *

import json


# Create your views here.



def premade(request):

    categories = Category.objects.all()
    labels = Variant.objects.all()
    products = Product.objects.all()
    boxes = GiftBox.objects.all()
    cards = Card.objects.all()
#     minMaxPrice = Product.objects.aggregate(
#         Min('discount_price'), Max('discount_price'))
#     # products = myFilter.qs

    data = {'products': products,
#             'labels': labels,
            'categories': categories,
            'boxes':boxes,
            'cards':cards,
#             'minMaxPrice': minMaxPrice,
            }
    if request.GET.get('cart_items'):
        prd_tot=0
        itm_tot=0
        cart = json.loads(request.GET.get('cart_items'))
        print("value in cart", cart)
        try:
            for prd in cart:
                itm_tot = (int(cart[prd]['quantity'])*int(cart[prd]['price']))
                cart[prd]['total_item_price']=itm_tot
                prd_tot=prd_tot+itm_tot
        except:
            pass

        request.session['cart'] = cart
        request.session['product_total_price'] = prd_tot
        return redirect('/')
    else:
        return render(request, 'product/premade.html', data)


def build_a_box(request):
    categories = Category.objects.all()
    labels = Variant.objects.all()
    products = Product.objects.all()
    boxes = GiftBox.objects.all()
    cards = Card.objects.all()
    gift_box_items = GiftBoxItem.objects.all()
    gift_box_items = GiftBoxItem.objects.filter(user=request.user,added2cart_status=False)
    if gift_box_items.exists():

        gift_box_items_qs=gift_box_items[0]
        print(gift_box_items_qs.card_type)
        gift_count=gift_box_items_qs.gift_items.all().count()
        for i in gift_box_items_qs.gift_items.all():
            print(i)
            print(i)
            print(i.product.image1)
            print(i.product.product.name)
            print(i.product.product.category)
    # print(items.box_type)
    # print(items.gift_items)
    # print(items.card_type)
    # print(items.card_message.recipient)
           
    data = {'products': products,
#             'labels': labels,
            'categories': categories,
            'boxes':boxes,
            'cards':cards,
            'items': gift_box_items_qs,
            'gift_count':int(gift_count)+2,
            }
   

    return render(request, 'product/build-a-box.html', data)





class SearchCategoryView(View):
    def get(self, *args, **kwargs):
        query = self.request.GET.get('q')
        cat = self.request.GET.get('cat-input')
        if cat:
            _object = Category.objects.get(name=cat)
            print(_object)
            cat_id = _object.id
            print(cat_id)
            
            cat_objects = ProductVariation.objects.filter(product__category=cat_id)
            products = cat_objects.filter(name__icontains=query)
        else:
            products = ProductVariation.objects.filter(name__icontains=query)
        context={
            'page_obj': products,
            'categories': Category.objects.all(),
            'cards': Card.objects.all(),
            'giftboxes': GiftBox.objects.all(),
            'products': Product.objects.all(),
            'variants': Variant.objects.all().values('variant').distinct(),
            'no_pagination':'no_pagination',
        }
        return render(self.request, 'product/category-page.html', context)



class ProductView(DetailView):
    model = ProductVariation
    template_name = 'product/product-page.html'
    context_object_name = 'product'

    def get_context_data(self, *args, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)
        product_rat = ProductVariation.objects.get(slug=self.kwargs['slug'])
        
        # getting product from current product variation to get colors and sizes
        product_name = ProductVariation.objects.get(slug=self.kwargs['slug']).product.name
        
        # getting all the colors from product variations
        # we want sizes that are available on the selected color
        product_color_variations = ProductVariation.objects.filter(product__name=product_name, size=self.object.size)
        colors = []
        for var in product_color_variations:
            col = var.color.colorCode
            if col not in colors:
                colors.append(col)
        # getting all the sizes from product variations
        # we want sizes that are available on the selected color
        product_size_variations = ProductVariation.objects.filter(product__name=product_name, color__name=self.object.color)
        sizes = []
        for var in product_size_variations:
            siz = var.size.size
            if siz not in sizes:
                sizes.append(siz)

        context['variation_colors'] = colors
        context['variation_sizes'] = sizes

        #cart and wishlist items 
        if self.request.user.is_authenticated:
            wishlist_items = WishItem.objects.filter(user=self.request.user)
            context['wish_items'] = [item.product.id for item in wishlist_items]

        return context
    

#function to opt for different size on product page
def sizeProduct(request):
    if request.method=='POST':
        size = request.POST.get('size')
        color = request.POST.get('color')
        variation_slug = request.POST.get('product')
        # we need to get product variation slug at the end, so we need product name and gender from this slug
        product_init = ProductVariation.objects.get(slug=variation_slug)
        product_name = product_init.product.name
        gender = product_init.product.get_gender_display()
        #making a list to join them
        str_list = [str(gender), str(product_name), str(color), str(size)]
        required_slug = slugify(('-').join(str_list))
        return HttpResponseRedirect(reverse('product:product-page', args=(required_slug,)))



class AddCategoryView(SuccessMessageMixin,CreateView):
    model = Category
    fields = ('__all__')
    template_name = 'add-items/add-category.html'
    success_message = "Category was added successfully"
    
    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('product:add-category')



class AddBoxSizeView(SuccessMessageMixin,CreateView):
    model = BoxSize
    fields = ('__all__')
    template_name = 'add-items/add-size.html'
    success_message = "Size was added successfully"
    
    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('product:add-size')


class AddVariantView(SuccessMessageMixin,CreateView):
    model = Variant
    fields = ('__all__')
    template_name = 'add-items/add-color.html'
    success_message = "Color was added successfully"
    
    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('product:add-color')


class AddProductView(SuccessMessageMixin,CreateView):
    model = Product
    fields = ('__all__')
    template_name = 'add-items/add-product.html'
    success_message = "Product was added successfully"

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('product:add-product')


class AddProductVariationView(SuccessMessageMixin,CreateView):
    model = ProductVariation
    fields = ('product', 'color', 'size', 'image1', 'image2', 'image3', 'image4', 'image5', 'price', 'stock')
    template_name = 'add-items/add-product-variation.html'
    success_message = "Product-Variation was added successfully"

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('product:add-product-variation')


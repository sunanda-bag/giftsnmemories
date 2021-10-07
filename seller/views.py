from django.shortcuts import render, reverse
from django.views import generic
from product.models import Category,ProductVariation
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponse
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from order.models import Order
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime
from django.http import HttpResponseRedirect

class ContactView(generic.View):
    def get(self, *args, **kwargs):
        return render(self.request, 'seller/contact.html')

class LegalView(generic.View):
    def get(self, *args, **kwargs):
        return render(self.request, 'seller/legal-info.html')

class DashboardView(generic.View):
    def get(self, *args, **kwargs):
        return render(self.request, 'seller/seller-dashboard.html')

#view to show all inventories including main categories, minimum products and all products
class AllInventoryView(generic.View):
    def get(self, *args, **kwargs):
        context = {
            'categories':Category.objects.all(),
            'min_inventories':ProductVariation.objects.filter(stock__lt=10).order_by('stock'),
            'all_inventories':ProductVariation.objects.all()
        }
        return render(self.request, 'seller/inventory.html', context)

#view to show all minimum available products (product variations)
class MinInventoryListView(generic.ListView):
    model = ProductVariation
    template_name = 'seller/inventory-list.html'
    context_object_name = 'products'
    extra_context = {'minimum_inventory':'min'}
    paginate_by = 12   
    extra_context ={'inv_type':'Minimum'}

    def get_queryset(self, *args, **kwargs):
        return ProductVariation.objects.filter(stock__lt=10).order_by('stock')

#view to show all available products (product variations)
class AllInventoryListView(generic.ListView):
    model = ProductVariation
    template_name = 'seller/inventory-list.html'
    context_object_name = 'products'
    paginate_by = 12   
    extra_context ={'inv_type':'All'}

    def get_queryset(self, *args, **kwargs):
        return ProductVariation.objects.all()

#view to show sub categories for main categories from all-inventory page
# class SubcategoryListView(generic.ListView):
#     model = SubCategory
#     template_name = 'seller/subcategory-list.html'
#     context_object_name = 'subcategories'

#     def get_queryset(self, *args, **kwargs):
#         cat_name = self.kwargs['name']
#         return SubCategory.objects.filter(category__name=cat_name)
    
    # def get_context_data(self, **kwargs):
    #     context = super(SubcategoryListView, self).get_context_data(**kwargs)
    #     context['category'] = self.kwargs['name']
    #     return context

# view to show all products (product variations) from each subcategory 
# class AllSubcategoryListView(generic.ListView):
#     model = ProductVariation
#     template_name = 'seller/inventory-list.html'
#     context_object_name = 'products'
#     paginate_by = 12

#     def get_queryset(self, *args, **kwargs):
#         subcat_id = self.kwargs['pk']
#         return ProductVariation.objects.filter(product__subCategory=subcat_id)

#     def get_context_data(self, **kwargs):
#         context = super(AllSubcategoryListView, self).get_context_data(**kwargs)
#         subcat = SubCategory.objects.get(id=self.kwargs['pk'])
#         context['inv_type'] = subcat 
#         context['cat_name'] = subcat.category.name
#         return context

# view to update product (product variation)
class ProductUpdateView(SuccessMessageMixin,generic.UpdateView):
    model = ProductVariation
    fields = ('product', 'color', 'size', 'image1', 'image2', 'image3', 'image4', 'image5', 'price', 'stock')
    template_name = 'add-items/add-product-variation.html'
    success_message = "Product updated successfully"

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('seller:product-update', args=[self.kwargs['pk']])

# view to delete product (product variation)
class ProductDeleteView(SuccessMessageMixin,generic.DeleteView):
    model = ProductVariation
    template_name = 'add-items/delete-product-variation.html'
    success_message = "Product Deleted successfully"

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('seller:inventory')

# inventory search view
class InventorySearchView(generic.ListView):
    model = ProductVariation
    template_name = 'seller/inventory-list.html'
    context_object_name = 'products'
    paginate_by = 12   
    extra_context ={'inv_type':'Searched'}

    def get_queryset(self, *args, **kwargs):
        q = self.request.GET.get('q')
        return ProductVariation.objects.filter(name__icontains=q)


class AllOrderView(generic.View):
    def get(self, *args, **kwargs):
        context = {
            'all_orders':Order.objects.filter(ordered=True).order_by('-id')[:5]
        }
        return render(self.request, 'seller/all-orders.html', context)

class OrderListView(LoginRequiredMixin,generic.ListView):
    model = Order
    context_object_name = 'orders'
    template_name = 'seller/order-list.html'
    paginate_by = 12

    def get_queryset(self):
        return Order.objects.filter(ordered=True).order_by('-id')

class OrderDetailView(LoginRequiredMixin,generic.DetailView):
    model = Order
    context_object_name = 'order'
    template_name = 'seller/order-detail.html'

def markDelivered(request, pk):
    order = Order.objects.get(id=pk)
    order.delivered = True
    order.deliveryDate = datetime.datetime.now()
    order.save()

    return HttpResponseRedirect(reverse('seller:order-list'))
from django.urls import path
from .views import *

app_name = 'seller'

urlpatterns = [
    # contact
    path('contact/', ContactView.as_view(), name='contact'),
    path('legal-info/', LegalView.as_view(), name='legal'),

    # dashboard and seller backend #
    path('dashboard/', DashboardView.as_view(), name='dashboard'), 
    path('inventory/', AllInventoryView.as_view(), name='inventory'), 
    path('min-inventory/', MinInventoryListView.as_view(), name='min-inventory'), 
    path('all-inventory/', AllInventoryListView.as_view(), name='all-inventory'), 
    # path('<str:name>/subcategories/',SubcategoryListView.as_view(), name='subcategory-list'),
    # path('<int:pk>/all-subcategory-inventory/', AllSubcategoryListView.as_view(), name='subcategory-products'),

    #update page
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),

    #delete page
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),

    #search page
    path('inventory/search/', InventorySearchView.as_view(), name='inventory-search'),

    #order pages
    path('all-orders/', AllOrderView.as_view(), name='all-orders'), 
    path('orders/', OrderListView.as_view(), name='order-list'), 
    path('orders/order/<int:pk>', OrderDetailView.as_view(), name='order-detail'), 
    path('orders/order-action/<int:pk>', markDelivered, name='mark-delivered')
]
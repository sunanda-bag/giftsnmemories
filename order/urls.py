from django.urls import path
from .views import *

app_name = 'order'

urlpatterns = [
    # path('wishlist/', WishlistView.as_view(), name='wishlist'),
    # path('cart/', CartView.as_view(), name='cart'),
    path('order-checkout/', orderCheckout, name='order-checkout'),
    # path('checkout/', CheckoutView.as_view(), name='checkout'),
    # path('Confirmation/', ConfirmationView.as_view(), name='confirmation'),

    path('add-box/', addBox, name='add-box'),
    path('add-card/', addCard, name='add-card'),
    path('delete-card/', deleteCard, name='delete-card'),
    path('add-to-gift-box/', addToGiftBox, name='add-to-gift-box'),
    path('add-card-to-box/', AddCardMessage, name='add-card-to-box'),

    # path('add-to-wishlist/', addToWishlist, name='add-to-wishlist'),
    # path('delete-from-wishlist/', deleteFromWishlist, name='delete-from-wishlist'),
    # path('add-to-cart/', addToCart, name='add-to-cart'),
    # path('delete-from-cart/', deleteFromCart, name='delete-from-cart'),
    # path('add-one-item/', addOneQuantity, name='add-one-quantity'),
    # path('delete-one-item/', deleteOneQuantity, name='delete-one-quantity'),

    # path('payment-success/', paymentSuccess, name='payment-success'),
    # path('payment-cancel/', paymentCancel, name='payment-cancel'),
]
from django.urls import path, include
from .views import *

app_name = 'gnm_users'

urlpatterns = [
    path('signin/', SigninView.as_view(), name='signin'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('signout/', signoutView, name='signout'),
    path('account/', AccountView.as_view(), name='cust-account'),
    path('orders/', CustomerOrdersListView.as_view(), name='cust-order-list'),
    path('order/<int:pk>', CustomerOrdersDetailView.as_view(), name='cust-order-detail'),
    path('account/<int:pk>/update', CustomerProfileUpdateView.as_view(), name='cust-profile-update'),
]
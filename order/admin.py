from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(BoxType)
admin.site.register(CardType)
admin.site.register(CardMessage)
admin.site.register(GiftItem)
admin.site.register(GiftBoxItem)
admin.site.register(Order)
admin.site.register(WishItem)
admin.site.register(OrderItem)


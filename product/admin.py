from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Variant)
admin.site.register(BoxSize)


@admin.register(GiftBox)
class GiftBoxAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tag', 'boxsize', 'active', 'price')
    list_editable=('active',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'brand', 'active','image_tag')
    list_editable=('active',)


@admin.register(ProductVariation)
class ProductVariationAdmin(admin.ModelAdmin):
    list_display = ('itemNumber','name','image_tag', 'product', 'variant', 'price', 'stock')



# @admin.register(PremadeProductVariation)
# class PremadeProductVariationAdmin(admin.ModelAdmin):
#     list_display = ('itemNumber','name','image_tag', 'products', 'price', 'stock')
admin.site.register(PremadeProduct)
admin.site.register(PremadeProductVariation)

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tag', 'active', )
    list_editable=('active',)






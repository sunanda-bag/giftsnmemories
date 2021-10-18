from django.db import models
import os
from django.utils.text import slugify
from django.db.models import Avg
from math import floor, ceil, modf
from django.contrib.auth.models import User
from django.utils.html import mark_safe

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='1. Categories'


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='2. Brands'


class Variant(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='3. Variants'


class BoxSize(models.Model):
    size = models.CharField(max_length=100)

    def __str__(self):
        return str(self.size)

    class Meta:
        verbose_name_plural='4. Box Sizes'


def gift_box_image(instance, filename):
    upload_to = 'giftboxes_files/{}/'.format(instance.boxsize.size)
    ext = filename.split('.')[-1]
    # get filename
    if instance.name:
        filename = '{}.{}'.format(instance.name, ext)
    return os.path.join(upload_to, filename)


class GiftBox(models.Model):

    boxsize = models.ForeignKey(BoxSize, on_delete=models.CASCADE, related_name='boxSize')
    name = models.CharField(max_length=250, unique=True)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=350, null=True, blank=True,
                                   default='lorem ipsum lorem ipsum lorem ipsum lorem ipsum')
    feature1 = models.CharField(max_length=250, null=True, blank=True,
                                default='lorem ipsum lorem ipsum lorem ipsum lorem ipsum')
    active = models.BooleanField(default=True)
    image = models.ImageField(upload_to=gift_box_image)

    def __str__(self):
        return f"{self.name} of {self.boxsize.size}"

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    class Meta:
        verbose_name_plural='5. Gift Box Types'


def card_image(instance, filename):
    upload_to = 'card_files/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.name:
        filename = '{}.{}'.format(instance.name, ext)
    return os.path.join(upload_to, filename)


class Card(models.Model):

    name = models.CharField(max_length=250, unique=True)
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    image = models.ImageField(upload_to=card_image)

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='6. Cards'


def product_image(instance, filename):
    upload_to = 'products_files/'.format(instance.category.name)
    ext = filename.split('.')[-1]
    # get filename
    if instance.name:
        filename = '{}.{}'.format(instance.name, ext)
    return os.path.join(upload_to, filename)


class Product(models.Model):

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='categoryProducts')
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, related_name='brandProducts')
    name = models.CharField(max_length=250, unique=True)
    description = models.CharField(max_length=350, null=True, blank=True,
                                   default='lorem ipsum lorem ipsum lorem ipsum lorem ipsum')
    feature1 = models.CharField(max_length=250, null=True, blank=True,
                                default='lorem ipsum lorem ipsum lorem ipsum lorem ipsum')
    feature2 = models.CharField(max_length=250, null=True, blank=True,
                                default='lorem ipsum lorem ipsum lorem ipsum lorem ipsum')
    feature3 = models.CharField(max_length=250, null=True, blank=True,
                                default='lorem ipsum lorem ipsum lorem ipsum lorem ipsum')

    active = models.BooleanField(default=True)
    image = models.ImageField(upload_to=product_image)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='7. Products'

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)
        product_variations = ProductVariation.objects.filter(product__name=self.name)
        if product_variations.count() > 0:
            for product in product_variations:
                if product.product.onSale:
                    discount_price = product.get_discount_price()
                    if isinstance(discount_price, float):
                        dec = modf(discount_price)[0]
                        if dec < 0.5:
                            price = floor(discount_price)
                        else:
                            price = ceil(discount_price)
                    else:
                        price = discount_price
                    product.discountPrice = price
                else:
                    product.discountPrice = product.price
                product.save()


def product_variation_image(instance, filename):
    upload_to = 'productvariation_files/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.name:
        filename = '{}.{}'.format(instance.name, ext)
    return os.path.join(upload_to, filename)


class ProductVariation(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='productVariations')
    slug = models.CharField(max_length=350, null=True, blank=True)
    itemNumber = models.PositiveIntegerField(unique=True, null=True, blank=True)
    name = models.CharField(max_length=500, null=True, blank=True)
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE)

    image1 = models.ImageField( upload_to=product_variation_image)
    image2 = models.ImageField(upload_to=product_variation_image, null=True, blank=True)

    price = models.PositiveIntegerField()
    discountPrice = models.PositiveIntegerField(null=True, blank=True)
    stock = models.PositiveIntegerField(default=10)

    def __str__(self):
        return f"{self.product.name} of {self.variant}"

    class Meta:
        verbose_name_plural='8. Product Variants'

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image1.url))

    def number(self):
        count = ProductVariation.objects.count()
        if count == 0:
            return 1
        else:
            last_object = ProductVariation.objects.order_by('-id')[0]
            return last_object.id + 1

    # def get_discount_price(self):
    #     product = self.product
    #     if product.onSale:
    #         if product.discount:
    #             percent = product.discount.discount
    #         elif product.deal:
    #             percent = product.deal.discount
    #         elif product.offer:
    #             percent = product.offer.discount
    #         else:
    #             percent = 0
    #         price_red = (percent/100) * self.price
    #         price = self.price - price_red
    #         return price
    #     else:
    #         return self.price

    def save(self, *args, **kwargs):
        if not self.itemNumber:
            self.itemNumber = self.number()
        if not self.name:
            self.name = self.product.name + '-' + self.variant.name
        if not self.slug:
            self.slug = slugify(self.name)
        # self.discountPrice = self.get_discount_price()
        super(ProductVariation, self).save(*args, **kwargs)

    # def avg_rating(self):
    #     #check if more than one rating for the product
    #     rating_count = Rating.objects.filter(product_variation__name=self.name).count()
    #     if rating_count > 1:
    #         ratings = Rating.objects.filter(product_variation__name=self.name).aggregate(Avg('rating'))
    #         ratings = ratings['rating__avg']
    #     elif rating_count == 1:
    #         ratings = Rating.objects.get(product_variation__name=self.name).rating
    #     else:
    #         ratings = 1

        # check if the number is float or not
        # if isinstance(ratings, float):
        #     dec = modf(ratings)[0]
        #     if dec < 0.5:
        #         rating = floor(ratings)
        #     else:
        #         rating = ceil(ratings)
        # else:
        #     rating = ratings
        # return rating


def premadeproduct_image(instance, filename):
    upload_to = 'premadeproducts_files/'.format(instance.category.name)
    ext = filename.split('.')[-1]
    # get filename
    if instance.name:
        filename = '{}.{}'.format(instance.name, ext)
    return os.path.join(upload_to, filename)


class PremadeProduct(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, unique=True)
    description = models.CharField(max_length=350, null=True, blank=True,
                                   default='lorem ipsum lorem ipsum lorem ipsum lorem ipsum')
    feature1 = models.CharField(max_length=250, null=True, blank=True,
                                default='lorem ipsum lorem ipsum lorem ipsum lorem ipsum')
    feature2 = models.CharField(max_length=250, null=True, blank=True,
                                default='lorem ipsum lorem ipsum lorem ipsum lorem ipsum')
    feature3 = models.CharField(max_length=250, null=True, blank=True,
                                default='lorem ipsum lorem ipsum lorem ipsum lorem ipsum')
    price = models.PositiveIntegerField(null=True, blank=True)
    active = models.BooleanField(default=True)
    image = models.ImageField(upload_to=premadeproduct_image)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='9. Premade Products'

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))


    # def save(self, *args, **kwargs):
    #     super(Product, self).save(*args, **kwargs)
    #     premadeproduct_variations = PremadeProductVariation.objects.filter(
    #         product__name=self.name)
    #     if premadeproduct_variations.count() > 0:
    #         for product in premadeproduct_variations:
    #             if product.product.onSale:
    #                 discount_price = product.get_discount_price()
    #                 if isinstance(discount_price, float):
    #                     dec = modf(discount_price)[0]
    #                     if dec < 0.5:
    #                         price = floor(discount_price)
    #                     else:
    #                         price = ceil(discount_price)
    #                 else:
    #                     price = discount_price
    #                 product.discountPrice = price
    #             else:
    #                 product.discountPrice = product.price
    #             product.save()

def premade_productvariation_image(instance, filename):
    upload_to = 'premade_productvariation_files/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.name:
        filename = '{}.{}'.format(instance.name, ext)
    return os.path.join(upload_to, filename)


class PremadeProductVariation(models.Model):
    products = models.ForeignKey(PremadeProduct, on_delete=models.CASCADE, related_name='premadeproductVariations')
    slug = models.CharField(max_length=350, null=True, blank=True)
    itemNumber = models.PositiveIntegerField(
        unique=True, null=True, blank=True)
    name = models.CharField(max_length=500)

    image1 = models.ImageField( upload_to=premade_productvariation_image)
    image2 = models.ImageField(
        upload_to=premade_productvariation_image, null=True, blank=True)

    price = models.PositiveIntegerField(null=True, blank=True)
    discountPrice = models.PositiveIntegerField(null=True, blank=True)
    stock = models.PositiveIntegerField(default=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='9. Premade Products Variation'

    def get_item_price(self):
        for i in self.products.count():
            self.price = self.price+ self.products[i].price
        return self.price

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image1.url))

    def number(self):
        count = PremadeProductVariation.objects.count()
        if count == 0:
            return 1
        else:
            last_object = PremadeProductVariation.objects.order_by('-id')[0]
            return last_object.id + 1

   

    def save(self, *args, **kwargs):
        if not self.itemNumber:
            self.itemNumber = self.number()
        # if not self.name:
        #     self.name = self.product.name + '-' + self.variant.name
        if not self.slug:
            self.slug = slugify(self.name)
        # self.discountPrice = self.get_discount_price()
        super(PremadeProductVariation, self).save(*args, **kwargs)


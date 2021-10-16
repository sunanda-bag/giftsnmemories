from os import stat_result
from django.db import models
from product.models import *
from django.contrib.auth.models import User


# Create your models here.
class BoxType(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gift_box = models.ForeignKey(GiftBox,on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.gift_box} of {self.gift_box.boxsize}"

    class Meta:
        verbose_name_plural='1. Box Type Selected'
    
    def get_box_price(self):
        return self.gift_box.price



class CardMessage(models.Model):
    
    card = models.OneToOneField(Card, on_delete=models.CASCADE, related_name='giftcardmsg')
    recipient = models.CharField(max_length=50, blank=True)
    sender = models.CharField(max_length=50, blank=True)
    card_content_front = models.TextField(max_length=500, blank=True)
    card_content_back = models.TextField(max_length=500,  blank=True)
    
    def __str__(self):
        return self.card.name

    class Meta:
        verbose_name_plural='2. Entered Card Messages'



class CardType(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card = models.OneToOneField(Card, on_delete=models.CASCADE,default=None)
    status = models.BooleanField(default=False)
    recipient = models.CharField(max_length=50, blank=True,null=True)
    sender = models.CharField(max_length=50, blank=True,null=True)
    card_content_front = models.TextField(max_length=500, blank=True,null=True)
    card_content_back = models.TextField(max_length=500,  blank=True,null=True)
    # card = models.ForeignKey(Card,on_delete=models.CASCADE)
    # card_message = models.ForeignKey(CardMessage,on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.card}"

    class Meta:
        verbose_name_plural='3. Card Type Selected'
    
    def get_card_price(self):
        return self.card.price



class GiftItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductVariation,on_delete=models.CASCADE)
    quantity = models.SmallIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product}"

    class Meta:
        verbose_name_plural='4. Gift Items Selected'

    def get_gift_item_price(self):
        return self.quantity * self.product.price


class GiftBoxItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    box_type = models.ForeignKey(BoxType,on_delete=models.CASCADE, blank=True,null=True)
    gift_items = models.ManyToManyField(GiftItem, blank=True)
    card_type = models.ForeignKey(CardType,on_delete=models.CASCADE, blank=True,null=True)
    # card_message = models.ForeignKey(CardMessage,on_delete=models.CASCADE, blank=True,null=True)
    added2cart_status = models.BooleanField(default=False)
    price = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural='5. Gift Box Items'

    def total_amount(self):
        total = 0
        for item in self.gift_items.all():
            total += item.get_gift_item_price()
        total += self.card_type.get_card_price()
        total += self.box_type.get_box_price()

        return total 

class WishItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductVariation,on_delete=models.CASCADE)
    quantity = models.SmallIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product}"

    class Meta:
        verbose_name_plural='6. Wishlist Items'

    def get_item_price(self):
        return self.quantity * self.product.discountPrice

class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductVariation,on_delete=models.CASCADE)
    quantity = models.SmallIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product}"

    class Meta:
        verbose_name_plural='7. Order Items'

    def get_item_price(self):
        return self.quantity * self.product.discountPrice

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    giftboxitems = models.CharField(max_length=2000,default=None)
    ordered = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)
    orderDate = models.DateTimeField(blank=True, null=True)
    deliveryDate = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=250, null=True, blank=True)
    mobile = models.PositiveIntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    city = models.CharField(max_length=250, null=True, blank=True)
    pincode = models.PositiveIntegerField(null=True, blank=True)
    quantity = models.SmallIntegerField(null=True, blank=True)
    price = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural='8. Orders'

    def total_amount(self):
        total = 0
        for item in self.items.all():
            total += item.get_item_price()
        return total 

from django.conf import settings
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

CATEGORY_CHOICES = (
    ('SN', 'snacks'),
    ('BR', 'breakfast'),
    ('LU', 'lunch'),
    ('BE', 'beverages')
)

LABEL_CHOICES = (
    ('S', 'students-choice'),
    ('N', 'new')
)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    college_id = models.CharField(max_length= 10)

    def __str__(self):
        return self.user.username


class Item(models.Model):
    name = models.CharField(max_length = 20)
    price = models.FloatField()
    photo = models.ImageField(upload_to='images/')
    category = models.CharField(choices = CATEGORY_CHOICES, max_length = 2, default= 'LU')
    label = models.CharField(choices = LABEL_CHOICES, max_length = 1, default= 'N')

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.photo.url
        except:
            url = ''
        return url


class Order(models.Model):
    student = models.ForeignKey(Student , on_delete=models.SET_NULL, blank=True, null=True)
    # """items = models.ManyToManyField(OrderItem)"""
    complete = models.BooleanField(default=False, null=True, blank=False)
    date_ordered = models.DateTimeField(auto_now_add=True, blank=True)
    transaction_id = models.CharField(max_length=16, null = True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([ item.get_total for item in orderitems])
        return total
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([ item.quantity for item in orderitems])
        return total
# """class Banners(models.Model):
#     image = models.ImageField(upload_to = 'banners')"""

class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True, blank=True)
    quantity = models.IntegerField(default=1)

    @property
    def get_total(self):
        total = self.item.price * self.quantity
        return total
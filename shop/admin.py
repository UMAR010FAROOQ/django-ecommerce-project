from django.contrib import admin
from .models import Product, Contact, Checkout, OrderUpdate

# Register your models here.
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Checkout)
admin.site.register(OrderUpdate)


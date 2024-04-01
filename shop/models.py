from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=300)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=1000)
    short_desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    color = models.CharField(max_length=10)
    stock = models.CharField(max_length=50, default="")
    fee = models.CharField(max_length=50, default="")
    image = models.ImageField(upload_to='shop/img', default="")

    def __str__(self):
        return str(self.product_name)


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    message = models.CharField(max_length=500, default="")


    def __str__(self):
        return str(self.name)

class Checkout(models.Model):
    order_id= models.AutoField(primary_key=True)
    items_json= models.CharField(max_length=5000)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=300)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    zip_code=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)
    

class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.order_id) +str(" ... ")+ str(self.update_desc)
from django.db import models



class Category(models.Model):
    name=models.CharField(max_length=80,default='غذا')

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=100,decimal_places=0)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)


    def __str__(self):
        return self.name
    

    
class Detail(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    pcs=models.PositiveIntegerField(default=1)
    

    def __str__(self):
        return f'{self.product}:{self.pcs}'
    
class CartItem(models.Model):
    user=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
    def total_price(self):
        return self.product.price * self.quantity

    

    
    
     


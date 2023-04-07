from django.db import models

# Create your models here.
class Product(models.Model):
    class Meta:
        db_table = "product"

    """
    상품 모델입니다.
    상품 코드, 상품 이름, 상품 설명, 상품 가격, 사이즈 필드를 가집니다.
    """
    code = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    price = models.IntegerField(default=0)
    sizes = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('F', 'Free'),
    )
    size = models.CharField(choices=sizes, max_length=1)

    inbound_quantity = models.IntegerField(default=0)
    outbound_quantity = models.IntegerField(default=0)
    stock_quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.code


class Inbound(models.Model):
    class Meta:
        db_table = "inbound" 
    
    code = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    ammount = models.IntegerField(default=0)


class Outbound(models.Model):
    class Meta:
        db_table = "outbound"       

    code = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    ammount = models.IntegerField(default=0)


class Invetory(models.Model):
    class Meta:
        db_table = "inventory"

    code = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='inventory')
    total_inbound_quantity = models.IntegerField(default=0)
    total_inbound_ammount = models.IntegerField(default=0)
    total_outbound_quantity = models.IntegerField(default=0)
    total_outbound_ammount = models.IntegerField(default=0)

from django.db import models

# Create your models here.



class Detail(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    email_address=models.EmailField(null=True,blank=True)
    phone=models.BigIntegerField(null=True,blank=True)
    invoice_number = models.PositiveIntegerField(default=0)
    joined_date = models.DateField(auto_now_add=True)
    joined_datetime = models.DateTimeField(auto_now_add=True)

    
        
    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):
        if not self.pk:
            self.invoice_number = Detail.objects.count() + 100
        super().save(*args, **kwargs)
  


PRODUCT_CHOICES=(
    ("Bike","Bike"),
    ("Car","Car"),
)


class productDetail(models.Model):
    customer=models.ForeignKey(Detail,on_delete=models.CASCADE)
    prod_name=models.CharField(choices=PRODUCT_CHOICES,max_length=100)
    quantity=models.IntegerField()
    rate=models.FloatField()
    amount=models.FloatField(null=True)


    
  




    
   
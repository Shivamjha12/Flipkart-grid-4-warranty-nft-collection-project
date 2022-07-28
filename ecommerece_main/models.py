from django.db import models
import uuid
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Create your models here.

class Createuserform(UserCreationForm):
    class Meta:
        models   = User
        fields   = ['username','first name','last name','email','password1','password2']
    def fullname(self):
        fullname = self.first_name + ' ' + self.last_name
        return fullname

class products(models.Model):
    seller = models.EmailField(null=False, blank=False)
    title = models.CharField(max_length=100)
    price = models.PositiveIntegerField(null=True, blank=True)
    img   = models.URLField(max_length=400)
    desc = models.TextField()
    warranty_in_months = models.PositiveIntegerField(null=True, blank=True)
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # def __unicode__(self):
    #     return self.prd_id
    
    def __str__(self):
        return self.title
    
class orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_buyed = models.ForeignKey(products, on_delete=models.CASCADE)
    ordered_date = models.DateTimeField(auto_now_add=True)
    order_id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    
    def __unicode__(self):
        return self.order_id

class nfts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_buy = models.ForeignKey(products, on_delete=models.CASCADE)
    token_id = models.CharField(max_length=50)
    nft = models.CharField(max_length=700)
    
    def __str__(self):
        return self.token_id 
from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(products)
admin.site.register(orders)
admin.site.register(nfts)
admin.site.register(wallet_details)
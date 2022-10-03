from django.contrib import admin

# Register your models here.

from .models import Crypto, Stock

admin.site.register(Crypto)
admin.site.register(Stock)

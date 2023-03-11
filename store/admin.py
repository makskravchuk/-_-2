from django.contrib import admin

from store import models

# Register your models here.

admin.site.register(models.User)
admin.site.register(models.Product)
admin.site.register(models.ProductCategory)
admin.site.register(models.Basket)

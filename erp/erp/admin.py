from django.contrib import admin
from .models import Product, Inbound, Outbound, Invetory

admin.site.register(Product)
admin.site.register(Inbound)
admin.site.register(Outbound)
admin.site.register(Invetory)
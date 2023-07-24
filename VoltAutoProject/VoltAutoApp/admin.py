from django.contrib import admin
from .models import Seller, Car, Comment, Automaker, CarModel

admin.site.register(Seller)
admin.site.register(Car)
admin.site.register(Comment)
admin.site.register(Automaker)
admin.site.register(CarModel)

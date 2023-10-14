from django.contrib import admin
from .models import Restaurant, Rentalcars

admin.site.register(Restaurant)
admin.site.register(Rentalcars)
# admin.py

from .models import ContactMessage

admin.site.register(ContactMessage)


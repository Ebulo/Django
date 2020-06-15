from django.contrib import admin

# Register your models here.
from .models import product, Contact

admin.site.register(product)
admin.site.register(Contact)

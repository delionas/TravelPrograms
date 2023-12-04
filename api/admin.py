from django.contrib import admin

# Register your models here.

from api.models import Problem
from api.models import Product

admin.site.register(Problem)
admin.site.register(Product)
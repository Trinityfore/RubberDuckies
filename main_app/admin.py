from django.contrib import admin
from .models import Accessories, Duck, Display
# Register your models here.

admin.site.register(Duck)
admin.site.register(Display)
admin.site.register(Accessories)
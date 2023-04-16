from django.contrib import admin

# Register your models here.
from .models import Search,location,coordinate
admin.site.register(Search)
admin.site.register(location)
admin.site.register(coordinate)

from django.contrib import admin
from . models import table, Review, tag

# Register your models here.

admin.site.register(table)
admin.site.register(Review)
admin.site.register(tag)
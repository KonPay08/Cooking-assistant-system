from django.contrib import admin
from .models import CategoryChoices,CookingName,Tag

admin.site.register(CategoryChoices)
admin.site.register(CookingName)
admin.site.register(Tag)

# Register your models here.

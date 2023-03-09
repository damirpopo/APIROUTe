from django.contrib import admin

from .models import Pet, Category, Status, TypeAnimal,Zakaz,Name

admin.site.register(Pet)
admin.site.register(Category)
admin.site.register(Status)
admin.site.register(TypeAnimal)
admin.site.register(Zakaz)
admin.site.register(Name)
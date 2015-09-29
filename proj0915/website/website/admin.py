from django.contrib import admin

from .models import Person, Pet

#brings Person class into admin site
admin.site.register(Person)

admin.site.register(Pet)
from django.contrib import admin

from .models import Tag,Item,OpeningHours,Reservation




admin.site.register(Tag)
admin.site.register(Item)
admin.site.register(OpeningHours)
admin.site.register(Reservation)
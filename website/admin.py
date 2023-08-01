from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Tag,Item,OpeningHours,Reservation
from import_export import resources





admin.site.register(OpeningHours)
admin.site.register(Reservation)


class TagResource(ImportExportModelAdmin):
    class Meta:
        model = Tag

class ItemResource(ImportExportModelAdmin):
    class Meta:
        model = Item

admin.site.register(Tag,TagResource)
admin.site.register(Item,ItemResource)

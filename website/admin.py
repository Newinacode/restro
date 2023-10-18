from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Tag,Item,OpeningHours,Reservation,Info
from import_export import resources





admin.site.register(OpeningHours)
admin.site.register(Reservation)
admin.site.register(Info)


class TagResource(ImportExportModelAdmin):
    class Meta:
        model = Tag

class ItemResource(ImportExportModelAdmin):
    search_fields = ['name__icontains', 'description__icontains', 'price','tag__name']
    class Meta:
        model = Item

        


admin.site.register(Tag,TagResource)
admin.site.register(Item,ItemResource)

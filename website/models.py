from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} {self.id}"

class Item(models.Model):
    tag  = models.ForeignKey(Tag,on_delete=models.CASCADE,related_name='items',blank=True,null=True)
    name = models.CharField(max_length=100,blank=True,null=True)
    price = models.CharField(max_length=10,blank=True,null=True)
    description = RichTextField(blank=True,null=True)

    def __str__(self):
        return f"{self.name} {self.tag} {self.price}"

class Reservation(models.Model):
    url = models.URLField(max_length = 200)


class Day(models.TextChoices):
    SUNDAY = "SUN",_("Sunday")
    MONDAY = "MON",_("Monday")
    TUESDAY = "TUE",_("Tuesday")
    WEDNESDAY = "WED",_("Wednesday")
    THURSDAY = "THU",_("Thursday")
    FRIDAY = "FRI",_("Friday")
    SATURDAY = "SAT",_("Saturday")

class OpeningHours(models.Model):
    day = models.CharField(max_length=3,choices=Day.choices,unique=True)
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    def __str__(self):
        return f'{self.day} {self.opening_time} {self.closing_time}'

class Info(models.Model):
    mobile_number = models.CharField(max_length=20,blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    instagram = models.URLField(blank=True,null=True)
    map_url = models.URLField(blank=True,null=True)
    tripadvisor = models.URLField(blank=True,null=True)
    tiktok = models.URLField(blank=True,null=True)
    facebook = models.URLField(blank=True,null=True)


    def save(self, *args, **kwargs):
        if not self.pk:
            Info.objects.all().delete()
        super(Info, self).save(*args, **kwargs)
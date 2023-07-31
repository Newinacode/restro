from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=100)


class Item(models.Model):
    tag  = models.ForeignKey(Tag,on_delete=models.CASCADE,related_name='items')
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2,max_digits=5)
    description = models.TextField()


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
    facebook= models.URLField(blank=True,null=True)
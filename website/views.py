from django.shortcuts import render
from .models import Item,Tag,OpeningHours,Reservation
# Create your views here.




def index(request):
    result = []
    tags = Tag.objects.all()

    for i in tags:
        tag = {
            "tag":i
        }
        item = i.items.all()
        tag["items"] = item
        result.append(tag)



    opening_hour  = OpeningHours.objects.all()
    reservation = Reservation.objects.first()
   
    
    context = {
        "result":result,
        "opening_hour":opening_hour,
        "reseration":reservation
    }
    print(tags)
    return render(request,'website/index.html',context)




def about(request):
    return render(request,'website/about.html')


def contact(request):
    return render(request,'website/contact.html')



def menu(request):
    result = []
    tags = Tag.objects.all()

    for i in tags:
        tag = {
            "tag":i
        }
        item = i.items.all()
        tag["items"] = item
        result.append(tag)

    context = {
        "result":result,
    }
    return render(request,'website/menu.html',context)

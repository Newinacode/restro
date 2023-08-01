from django.shortcuts import render
from .models import Item,Tag
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

    print(result)
    
    context = {
        "result":result
    }
    print(tags)
    return render(request,'website/index.html',context)




def about(request):
    return render(request,'website/about.html')


def contact(request):
    return render(request,'website/contact.html')
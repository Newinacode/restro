from .views import index,about,contact,menu


from django.urls import path

urlpatterns = [
    path('',index,name='index'),
    path('about',about,name="about"),
    path('contact',contact,name="contact"),
    path('menu',menu,name="menu")
]
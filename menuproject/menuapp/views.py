from django.shortcuts import render
from .models import Menu
# Create your views here.
'''
def menu(request):
    newmenu = {'mains' : [
        {'name' : 'falafel', 'price' : "23"},
        {'name' : 'shwarma', 'price' : "44"},
        {'name' : 'gyro', 'price' : "23"},
        {'name' : 'sandwich', 'price' : "2322"}
    ]}
    return render(request, 'menu.html', newmenu)
    
'''
def menu_by_id(request):
    newmenu = Menu.objects.all()
    newmenu_dict = {'menu' : newmenu}
    return render(request, 'menu_card.html', newmenu_dict)
from django.shortcuts import render

# Create your views here.
def menu(request):
    newmenu = {'mains' : [
        {'name' : 'falafel', 'price' : "23"},
        {'name' : 'shwarma', 'price' : "44"},
        {'name' : 'gyro', 'price' : "23"},
        {'name' : 'sandwich', 'price' : "2322"}
    ]}
    return render(request, 'menu.html', newmenu)
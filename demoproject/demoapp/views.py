from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.


def home(request):
    path = request.path
    response = HttpResponse('this works!')
    return response


def pathview(request, name, id):
    return HttpResponse('Name:{} UserID:{}'.format(name,id))

def qryview(request):
    name = request.GET['name']
    id = request.GET['id']
    return HttpResponse('Name:{}, UserID:{}'.format(name,id))

def showform(request):
    return render(request, 'form.html')

def getform(request):
    if request.method == 'POST':
        id = request.POST['id']
        name = request.POST['name']
        return HttpResponse('Name:{}, UserID:{}'.format(name,id))
    
def menuitems(request, dish):
    items = {

        'pasta':'good type of food',
        'flafel' : 'spicy kind of food',
        'cheesecake' : 'i dunno about this one'
    }
    description = items[dish]
    return HttpResponse(f'<h2> {dish} </h2>' + description)


def menu_item_view(request, id):
    return HttpResponse('Menu_item_number:{}'.format(id))

def index(request):
    context = {'user' : "admin"}
    return render(request, 'index.html', context)

def hello(request, name):
    context = {"name" : name}
    return render(request, 'hello.html', context)

def about(request):
    about_content = {'about' : "this is little lemon" }
    return render(request, 'about.html', about_content)


def person(request):
    person={'name':'Roger', 'profession':'Teacher'}
    return render(request,'person.html', person)

def myview(request):
    langs = ['Python', 'Java', 'PHP', 'Ruby', 'Rust']
    return render(request, 'langs.html', {'langs' : langs})
    


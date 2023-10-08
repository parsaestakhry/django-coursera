from django.urls import path,re_path
from . import views
app_name = 'demoapp'

urlpatterns = [
    path('' , views.home, name='home'),
    path('getuser/<name>/<id>', views.pathview, name='pathview'),
    path('getuser/' , views.qryview, name='qryview'),
    path('showform/', views.showform, name='showform'),
    path('dishes/<str:dish>' , views.menuitems),
    re_path(r'^menu_item/([0-9]{2})/$' , views.menu_item_view, name='menu_item_view'),
    path('index/', views.index, name='index'),
    path('hello/<str:name>/', views.hello, name='hello'),
    path('about/', views.about, name='about')

]

from django.urls import path,include
from django.conf.urls import url
from . import views
urlpatterns=[
    path('',views.index,name="index"),
    path('addproduit',views.addproduit,name="addproduit"),
    path('viewforni',views.viewfor,name="viewforni"),
    path('viewcomamnde',views.viewcommande,name="viewcomamnde"),
    path('comander',views.addcommande,name="comander")
]
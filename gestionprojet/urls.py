from django.urls import path,include
from django.conf.urls import url
from . import views
urlpatterns=[
    path('',views.login,name="login"),
    path('home',views.home,name="home"),
    path('viewproject/<id>',views.viewproject,name="viewproject"),
    path('deleteproject/<id>',views.deleteproject,name="deleteproj"),
    path('addproject',views.addproject,name="addproj"),
    path('addtask/<id>',views.addTask,name="addtask"),
    path('deletetask/<id>',views.deleteTask,name="deletetask"),
    path('cpmlte/<id>',views.cpmlte,name="cpmlte"),
    path('editp/<id>',views.editeproject,name="editp"),
    path('edittask/<id>',views.edittask,name="edittask"),
    path('logout',views.logout,name="logout"),
    path('inscrir',views.signup,name="inscrir")
]

from django.contrib import admin
from django.urls import path
from myApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentPage/', studentPage, name= "studentPage"),
    path('teacherPage/', teacherPage, name= "teacherPage" ),
    path('studentAdd/', studentAdd, name= "studentAdd" ),
    path('studentEdit/', studentEdit, name= "studentEdit" ),
    path('studentIdCall/<str:myid>', studentIdCall, name= "studentIdCall" ),
]

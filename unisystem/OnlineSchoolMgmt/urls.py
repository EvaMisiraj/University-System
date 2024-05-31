
from django.contrib import admin
from django.urls import path
from app.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home1, name='home1'),
    path('portal/',portal ,name='portal'),
   
    path('addAttendance/', addAttendance,name='addAttendance'),
   
    path('addMarks/', addMarks,name='addMarks'),
 
    path('addNotice/', addNotice,name='addNotice'),

    path('login/', loginPage,name='login'),
    path('logout/', logoutPage,name='logout'),
]

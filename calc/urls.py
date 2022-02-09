from django.urls import include, path
from . import views
urlpatterns = [
    path('',views.index,name="home"),
    path('get-gpa-calc/',views.index),
    path('getgpa/',views.calculategpa),  
]

from django.urls import path
from .import views

urlpatterns = [
    path('in/',views.index, name="home"),
    path('list/',views.list_stu, name="list"),
]

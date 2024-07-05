
from django.urls import path
from . import views
urlpatterns = [

    path('add/',views.add_cetagory,name='add_cetagory')
]

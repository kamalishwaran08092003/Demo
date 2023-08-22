from django.urls import path
from .import views

urlpatterns=[
    path('book/',views.book,name='book'),
     path('student/',views.index1,name='index'),
   
]

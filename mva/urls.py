from django.urls import path
from . import views


urlpatterns =[
    path('', views.mainpage, name="mainpage"),
    path('homepage/', views.homepage, name="homepage")
    
]
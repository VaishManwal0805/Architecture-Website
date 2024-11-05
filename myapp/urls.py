from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.home,name='home'),
    #path("contact",views.contact_view,name='contact'),
    path('contact/', views.contact, name='contact'),
    path("services",views.services,name='services'),
    path("projects",views.projects,name='projects'),
    path("projects/kindergarten",views.kindergarten,name='kindergarten'),
    path("projects/Minimalist Architecture",views.minimalist_arch,name="minimalist_arch"),
    path("projects/Classic Contemporary Architecture",views.classic_cont,name="classic_cont"),
    path("projects/Morico Cafe",views.morico_c,name="morico_cafe"),
    path('projects/Hide & Seek Bar And Restaurant',views.restaurant_hs,name="restaurant")
]



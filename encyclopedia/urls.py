from django.urls import path
from . import views

app_name = "wiki"
urlpatterns = [
    
    path("", views.index, name="index"),
    path("randomPage", views.randomPage, name = "randomPage"),
    path("search", views.search, name = "search"),
    path("create", views.create, name = "create"),
    path("edit/<str:name>", views.edit, name = "edit"),
    path("wiki/<str:name>", views.page, name = "page")   
]

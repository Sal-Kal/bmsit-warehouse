from django.urls import path
from . import views


# route_paths for the database app

urlpatterns = [
    path('add/new/conference/', views.addConference),
    path('get/all/conference/', views.getConferences),
    path('get/all/journal/', views.getJournals),
    path('get/all/book/', views.getBooks),
]
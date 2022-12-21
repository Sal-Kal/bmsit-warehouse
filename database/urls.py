from django.urls import path
from . import views


# route_paths for the database app

urlpatterns = [
    path('add/new/journal/', views.addJournal),
    path('get/all/journal/', views.getJournals),
]
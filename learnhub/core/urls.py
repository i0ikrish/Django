from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('edit/<int:id>/', views.edit_note, name='edit_note'),
]
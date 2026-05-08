from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('edit/<int:id>/', views.edit_note, name='edit_note'),
    path('delete/<int:id>/', views.delete_note, name='delete_note'),
    path('pdfs/', views.upload_pdf, name='upload_pdf'),
    path('note/<int:id>/', views.note_detail, name='note_detail'),
]
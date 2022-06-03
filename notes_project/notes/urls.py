from django.urls import path
from . import views

urlpatterns = [
    path('', views.notes, name='notes'),
    path('notes/<str:pk>/', views.note_detail, name='note-detail'),
    path('add-note/', views.add_note, name='add-note'),
    path('update-note/<str:pk>/', views.update_note, name='update-note'),
    path('delete-note/<str:pk>/', views.delete_note, name='delete-note'),
]

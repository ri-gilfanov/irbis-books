from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_search, name='book_search'),
    path('book_download/', views.book_download, name='book_download'),
]
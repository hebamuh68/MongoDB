from django.urls import path
from .views import search_views, insert_views

urlpatterns = [
    path('', search_views, name='search'),
    path('insert/', insert_views, name='insert'),
]

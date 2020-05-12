from django.urls import path
from .views import create_snippet, get_list_of_snippets


urlpatterns = [
    path('', create_snippet),
    path('all/', get_list_of_snippets)
]
from django.urls import path
from .views import jokes_render, joke_add_one

urlpatterns = [
    path('', jokes_render, name='jokes_render'),
    path('new_one/<int:joke_id>', joke_add_one, name='joke_add_one')
]
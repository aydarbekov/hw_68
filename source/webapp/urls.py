from django.urls import path
from .views import index_view

app_name = 'webapp'

urlpatterns = [
    path('index/', index_view, name='index'),
]
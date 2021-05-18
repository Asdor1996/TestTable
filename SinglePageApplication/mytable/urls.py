
from django.urls import path
from .views import table_print

urlpatterns = [
    path('', table_print),
]

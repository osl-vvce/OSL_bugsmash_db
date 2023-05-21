from .views import index,conn_db
from django.urls import path

urlpatterns = [
    path('', index),
    path('button-click/',conn_db)

]
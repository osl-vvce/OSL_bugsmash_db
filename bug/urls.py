from .views import index,conn_db,select
from django.urls import path

urlpatterns = [
    path('', index),
    path('button-click/',conn_db),
    path('select/',select)

]
from django.shortcuts import render
from django.http import HttpResponse
from .models import person
import pymysql
# Create your views here.

data = person.objects.all()

def index(request):
    context = {
        'model_data': data,
    }

    
    return render(request, 'index.html', context)


def conn_db(request):
    connection = pymysql.connect(
    host='db-mysql-blr1-69476-do-user-14046288-0.b.db.ondigitalocean.com',
    user='doadmin',
    password='AVNS_YijafuhF4slggX8rKO7',
    database='bugsmash',
    port=25060
)

    if connection:
        return HttpResponse('The server did not connect')

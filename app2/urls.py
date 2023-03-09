from app2.views import *
from django.urls import path
app_name='def'
urlpatterns=[
    path('hari/',hari,name='hari'),
    path('anil/',anil,name='anil'),
]
from app1.views import *
from django.urls import path
app_name='abc'
urlpatterns=[
    path('sam/',sam,name='sam'),
    path('ram/',ram,name='ram'),
]
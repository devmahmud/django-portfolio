from django.urls import path
from . import views

app_name = 'job'

urlpatterns = [
    # None
    path('', views.index, name='index'),
]

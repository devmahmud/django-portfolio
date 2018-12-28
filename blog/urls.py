from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # None
    path('', views.index, name='index'),
    path('<int:post_id>/', views.detail, name='detail'),
]

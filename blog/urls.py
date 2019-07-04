from django.urls import paths
from . import views

urlpatterns = [
path('', views.post_list, name='post_list')
]

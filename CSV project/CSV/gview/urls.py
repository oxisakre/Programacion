from re import template
from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainView.as_view(template_name='templates/main.html'), name='main'),
    path('table', views.idListView.as_view(), name='Table'),
]
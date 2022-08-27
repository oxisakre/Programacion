from re import template
from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainView.as_view(template_name='templates/main.html'), name='main'),
    path('page1', views.MainView.as_view(template_name='templates/main.html'), name='page1'),
    path('page2', views.MainView.as_view(template_name='templates/main.html'), name='page2'),
    path('page3', views.MainView.as_view(template_name='templates/main.html'), name='page3'),
    path('list', views.idListView.as_view(), name='data'),
]
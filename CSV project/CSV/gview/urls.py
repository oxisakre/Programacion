from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='testing'),
    path('information', views.idListView.as_view(), name='information'),

]
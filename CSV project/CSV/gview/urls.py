from django.urls import path
from . import views

urlpatterns = [
    path('', views.idListView.as_view(), name='testing'),
    path('list', views.idListView.as_view(), name='data'),

]
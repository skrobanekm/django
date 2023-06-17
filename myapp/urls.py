from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index'),
path('chovatele/', views.ChovateleListView.as_view(), name='chovatele_list'),
path('chovatele/<int:pk>', views.ChovatelDetailView.as_view(), name='chovatel_detail'),
]
from django.urls import path, include
from . import views

urlpatterns=[
    path('',views.index, name='index'),
    path('property/<int:property_id>/', views.property_detail, name='property_detail'),

]


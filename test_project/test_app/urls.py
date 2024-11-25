from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='first'),
    path('page02/<str:cookie>/', views.user, name='second'),
    path('page03/', views.createproject, name='create-project'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='first'),
    path('User/<str:cookie>/', views.user, name='second'),
    path('Create/', views.createproject, name='create-project'),
    path('Update/<str:pk>', views.updateproject, name='update-project'),
    path('Delete/<str:pk>', views.deleteproject, name='delete-project'),
    path('Services/', views.services, name='services'),
    path('About/', views.about, name='about'),
    path('Contacts/', views.contact, name='contact'),
]
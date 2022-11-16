from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='uchaguzi-home'),
    path('candidates/', views.candidates, name='uchaguzi-candidates')
]
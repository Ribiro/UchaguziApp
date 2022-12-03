from django.urls import path
from . import views
from .views import POResultCreateView

urlpatterns = [
    path('', views.home_page, name='uchaguzi-home'),
    path('candidates/', views.candidates, name='uchaguzi-candidates'),
    path('post/<pk>/', POResultCreateView.as_view(), name='post-po-result'),
    path('confirm_publish/', views.confirm_publish_results, name='confirm-publish-po-results'),
    path('publish/', views.publish_results, name='publish-po-results')
]
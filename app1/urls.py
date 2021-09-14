from django.urls import path
from . import views
urlpatterns = [
    path('', views.test_celery_view, name='test_celery_url'),
]

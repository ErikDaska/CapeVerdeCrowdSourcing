from django.urls import path
from . import views  # Importing views from your 'core' app

urlpatterns = [
    path('', views.index, name='index'),
    path('savePhrase/', views.savePhrase, name='savePhrase'),
]
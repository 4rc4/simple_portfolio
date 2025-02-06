from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),  # Ana sayfa
    path('models/', views.model_list, name='models'),  # Modeller listesi
    path('models/<int:id>/', views.model_detail, name='model_detail'),  # Model detayları
]

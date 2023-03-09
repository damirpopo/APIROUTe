from django.urls import path
from . import views

urlpatterns = [
    path('pet/', views.PetView.as_view()),
    path('pet/<str:pk>/', views.Pet2View.as_view()),
    path('zakaz/', views.ZakazView.as_view()),
    path('zakaz/<str:pk>/', views.Zakaz2View.as_view()),
]
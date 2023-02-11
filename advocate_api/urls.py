from django.urls import path

from . import views

urlpatterns = [
    path('', views.apiOverview, name="apiOverview"),
    path('advocates/', views.advocates, name="advocates"),
    path('advocate_details/<str:pk>/', views.advocatesDetails, name="advocate_details"),
    
]

    
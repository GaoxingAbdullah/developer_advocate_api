from django.urls import path

from . import views

urlpatterns = [
    path('', views.apiOverview, name="apiOverview"),
    path('advocate_list/', views.advocate_list, name="advocate_list"),
    path('advocate_details/<str:pk>/', views.advocate_details, name="advocate_details"),
    path('advocate_create/', views.advocate_create, name="advocate_create"),
    path('advocate_update/<str:pk>/', views.advocate_update, name="advocate_update"),
]

    
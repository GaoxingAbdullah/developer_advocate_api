from django.urls import path

from . import views

urlpatterns = [
    path('', views.apiOverview, name="apiOverview"),
    path('advocate-list/', views.advocate_list, name="advocate-list"),
    path('advocate-details/<str:pk>/', views.advocate_details, name="advocate-details"),
    path('advocate-create/', views.advocate_create, name="advocate-create"),
    path('advocate-update/<str:pk>/', views.advocate_update, name="advocate-update"),
    path('advocate-delete/<str:pk>/', views.advocate_delete, name="advocate-delete"),
]

    
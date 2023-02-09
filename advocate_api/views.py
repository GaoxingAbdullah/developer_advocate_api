from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def apiOverview(request):
    
    api_urls = {
        'Advocates': '/advocates/',
        'Advocates Details': '/Advocates/<str:pk>/',
        'Advocates Search' : '/advocates/<str:username>/',
        'Advocates Update': '/advocates/<str:pk>/',
        'Advocates Delete ': '/advocates/<str:pk>/',
    }
    
    return Response(api_urls)

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Advocate
from .serializers import AdvocateSerializer


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

@api_view(['GET'])
def advocates(request):
    
    advocate = Advocate.objects.all()
    serializer = AdvocateSerializer(advocate, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def advocatesDetails(request, pk):
    
    advocate = Advocate.objects.get(id=pk)
    serializer = AdvocateSerializer(advocate, many=False)

    return Response(serializer.data)
    
    

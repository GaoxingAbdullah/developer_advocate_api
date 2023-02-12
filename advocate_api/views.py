from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Advocate
from .serializers import AdvocateSerializer


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Advocate List': '/advocate_list/',
        'Advocate Details': '/advocate-detials/<str:pk>/',
        'Advocate Search' : '/advocate-search/<str:username>/',
        'Advocate Create': '/advocate-create/',
        'Advocate Update': '/advocate-update/<str:pk>/',
        'Advocate Delete ': '/advocate-delete/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def advocate_list(request):
    advocate = Advocate.objects.all()
    serializer = AdvocateSerializer(advocate, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def advocate_details(request, pk):
    advocate = Advocate.objects.get(id=pk)
    serializer = AdvocateSerializer(advocate, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def advocate_create(request):
    serializer = AdvocateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def advocate_update(request, pk):
    advocate = Advocate.objects.get(id=pk)
    serializer = AdvocateSerializer(instance=advocate, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

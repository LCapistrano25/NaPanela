from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated  
from country.models import Country
from country.serializers import CountryModelSerializer

class CountryListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Country.objects.all()
    serializer_class = CountryModelSerializer

class CountryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Country.objects.all()
    serializer_class = CountryModelSerializer
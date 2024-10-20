from django.urls import path
from country.views import CountryListCreateAPIView, CountryRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('countries/', CountryListCreateAPIView.as_view(), name='countries'),
    path('countries/<int:pk>/', CountryRetrieveUpdateDestroyAPIView.as_view(), name='country'),
]


from rest_framework.serializers import ModelSerializer

from core.mixins import SaveSerializerMixin
from country.models import Country

class CountryModelSerializer(SaveSerializerMixin, ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name', 'initials', 'status', 'created_by_name', 'created_at', 
                  'updated_by_name', 'updated_at']
from rest_framework.serializers import ModelSerializer
from core.mixins import SaveSerializerMixin
from categories.models import Category

class CategoryModelSerializer(SaveSerializerMixin, ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'status', 'created_by_name', 'created_at', 'updated_by_name', 'updated_at']
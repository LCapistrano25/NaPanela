from django.contrib import admin
from rest_framework import serializers

from django.db import models

# Mixin para identificar e registrar o usuário responsável pela criação e atualização de algum dado
class SaveModelMixin:
    def save_model(self, request, obj, form, change):
        user = request.user

        if not obj.pk:
            obj.created_by = user
        else:
            obj.updated_by = user
        super().save_model(request, obj, form, change)


class SaveSerializerMixin(serializers.ModelSerializer):

    created_by_name = serializers.CharField(source='created_by.username', read_only=True)
    updated_by_name = serializers.CharField(source='updated_by.username', read_only=True)
    
    product_name = serializers.CharField(
        source='product_identifier_id.product_name', 
        read_only=True
    )

    def save(self, **kwargs):
        user = self.context['request'].user

        if self.instance is None:
            self.validated_data['created_by'] = user
        else:
            self.validated_data['updated_by'] = user

        return super().save(**kwargs)

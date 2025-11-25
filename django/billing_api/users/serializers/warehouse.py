from rest_framework import serializers
from ..models import Warehouse

class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ['code', 'name', 'address', 'city', 'created_at', 'updated_at']

    def create(self, value):
        if '' in value:
            raise serializers.ValidationError("All fields must be filled.")
        return value
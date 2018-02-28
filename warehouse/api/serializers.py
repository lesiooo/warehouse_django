from rest_framework import serializers
from warehouse.models import SemiFinishedItem, FinishedProduct

class SemiFinishedItemSerializer(serializers.ModelSerializer):

    url = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = SemiFinishedItem
        fields = [
            'url',
            'id',
            'name',
            'slug',
            'quantity',
            'category',
            'producer',
            'price',
        ]
        read_only_fields = ['slug']

    def get_url(self, obj):
        request = self.context.get('request')
        return obj.get_api_url(request=request)


class FinishedProductSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = FinishedProduct
        fields = [
            'url',
            'id',
            'name',
            'slug',
            'price',
            'EAN_code',
            'quantity',
        ]

    def get_url(self, obj):
        request = self.context.get('request')
        return obj.get_api_url(request=request)

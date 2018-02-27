from rest_framework import serializers
from warehouse.models import SemiFinishedItem

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

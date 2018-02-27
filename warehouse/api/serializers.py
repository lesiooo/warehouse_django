from rest_framework import serializers
from warehouse.models import SemiFinishedItem

class SemiFinishedItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = SemiFinishedItem
        fields = [
            'id',
            'name',
            'slug',
            'quantity',
            'category',
            'producer',
            'price',
        ]
        read_only_fields = ['slug']

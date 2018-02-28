from rest_framework import generics, mixins
from warehouse.models import SemiFinishedItem, FinishedProduct
from .serializers import SemiFinishedItemSerializer, FinishedProductSerializer


class SemiFinishedItemRUDView(generics.RetrieveUpdateDestroyAPIView):

    lookup_field = 'id'
    serializer_class = SemiFinishedItemSerializer
    queryset = SemiFinishedItem.objects.all()

    def get_queryset(self):
        return self.queryset

    def get_serializer_context(self, *args, **kwargs):
        return {'request': self.request}


class SemiFinishedItemAPIView(mixins.CreateModelMixin, generics.ListAPIView):

    lookup_field = 'id'
    serializer_class = SemiFinishedItemSerializer
    #queryset = SemiFinishedItem.objects.all()

    def get_queryset(self):
        return SemiFinishedItem.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {'request': self.request}


class FinishedProductRUDView(generics.RetrieveUpdateAPIView):

    lookup_field = 'id'
    serializer_class = FinishedProductSerializer
    queryset = FinishedProduct.objects.all()

    def get_queryset(self):
        return self.queryset

    def get_serializer_context(self, *args, **kwargs):
        return {'request': self.request}

class FinishedProductAPIView(generics.ListAPIView):
    serializer_class = FinishedProductSerializer

    def get_queryset(self):
        return FinishedProduct.objects.all()
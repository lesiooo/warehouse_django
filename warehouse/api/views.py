from rest_framework import generics, mixins
from warehouse.models import SemiFinishedItem
from .serializers import SemiFinishedItemSerializer


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
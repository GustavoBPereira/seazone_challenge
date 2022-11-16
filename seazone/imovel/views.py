from django.http import Http404
from rest_framework import serializers, viewsets
from rest_framework.response import Response

from seazone.imovel.models import Imovel


class ImovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imovel
        fields = '__all__'
        read_only_fields = ('code',)


class ImovelViewSet(viewsets.ModelViewSet):
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except Http404:
            return super(ImovelViewSet, self).list(request, *args, **kwargs)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

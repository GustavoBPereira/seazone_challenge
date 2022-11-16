from django.http import Http404
from rest_framework import serializers, viewsets
from rest_framework import status
from rest_framework.response import Response

from seazone.anuncio.models import Anuncio


class AnuncioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anuncio
        fields = '__all__'


class AnuncioViewSet(viewsets.ModelViewSet):
    queryset = Anuncio.objects.all()
    serializer_class = AnuncioSerializer

    def destroy(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except Http404:
            return super(AnuncioViewSet, self).list(request, *args, **kwargs)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

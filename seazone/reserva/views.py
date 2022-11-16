from django.http import Http404
from rest_framework import serializers, viewsets
from rest_framework.response import Response

from seazone.reserva.models import Reserva


class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'
        read_only_fields = ('code', 'total_price')

    def create(self, validated_data):
        price = self.context['request'].data.get('price', False)
        if price:
            total_price = validated_data['anuncio'].imovel.clean_value + int(price)
        else:
            raise serializers.ValidationError({'price': 'Campo required'})
        validated_data['total_price'] = total_price
        return super(ReservaSerializer, self).create(validated_data)

    def validate(self, data):
        if data.get('anuncio'):
            guest_limit = data.get('anuncio').imovel.guest_limit
        else:
            guest_limit = self.instance.anuncio.imovel.guest_limit

        if data.get('guest_quantity'):
            guest_quantity = data.get('guest_quantity')
        else:
            guest_quantity = self.instance.guest_quantity

        if data.get('check_in'):
            check_in = data.get('check_in')
        else:
            check_in = self.instance.check_in

        if data.get('check_out'):
            check_out = data.get('check_out')
        else:
            check_out = self.instance.check_out

        if guest_quantity > guest_limit:
            raise serializers.ValidationError(
                {"guest_limit": f"O limite de convidados para este imóvel é: {guest_limit}"})
        if check_in >= check_out:
            raise serializers.ValidationError({"check_in": "Check out precisa ser depois do check in"})
        return data


class ReservasViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except Http404:
            return super(ReservasViewSet, self).list(request, *args, **kwargs)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

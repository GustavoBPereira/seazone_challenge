import uuid

from django.db import models

from seazone.anuncio.models import Anuncio


class Reserva(models.Model):
    code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    anuncio = models.ForeignKey(Anuncio, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    total_price = models.IntegerField()
    comment = models.TextField(null=True, blank=True)
    guest_quantity = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def to_json(self):
        return {
            'code': str(self.code),
            'anuncio': self.anuncio,
            'check_in': self.check_in,
            'check_out': self.check_out,
            'total_price': self.total_price,
            'comment': self.comment,
            'guest_quantity': self.guest_quantity,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

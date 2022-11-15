from django.db import models

from seazone.imovel.models import Imovel


class Anuncio(models.Model):
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE)
    platform = models.CharField(max_length=255)
    platform_fee = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def to_json(self):
        return {
            'imovel': self.imovel,
            'platform': self.platform,
            'platform_fee': self.platform_fee,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

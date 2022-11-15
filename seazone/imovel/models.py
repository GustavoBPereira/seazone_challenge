import uuid

from django.db import models


class Imovel(models.Model):
    code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    guest_limit = models.IntegerField()
    bathroom_quantity = models.IntegerField()
    is_pet_friendly = models.BooleanField()
    clean_value = models.IntegerField()
    activation_date = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def to_json(self):
        return {
            'code': str(self.code),
            'guest_limit': self.guest_limit,
            'bathroom_quantity': self.bathroom_quantity,
            'is_pet_friendly': self.is_pet_friendly,
            'clean_value': self.clean_value,
            'activation_date': self.activation_date,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

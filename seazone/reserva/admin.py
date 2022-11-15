from django.contrib import admin

from seazone.reserva.models import Reserva


class ReservaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Reserva, ReservaAdmin)

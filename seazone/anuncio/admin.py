from django.contrib import admin

from seazone.anuncio.models import Anuncio


class AnuncioAdmin(admin.ModelAdmin):
    pass


admin.site.register(Anuncio, AnuncioAdmin)

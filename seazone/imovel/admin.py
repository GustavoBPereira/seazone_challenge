from django.contrib import admin

from seazone.imovel.models import Imovel


class ImovelAdmin(admin.ModelAdmin):
    pass


admin.site.register(Imovel, ImovelAdmin)

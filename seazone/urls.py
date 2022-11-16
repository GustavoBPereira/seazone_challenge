from django.contrib import admin

from django.urls import path, include
from rest_framework import routers

from seazone.anuncio.views import AnuncioViewSet
from seazone.imovel.views import ImovelViewSet
from seazone.reserva.views import ReservasViewSet

router = routers.DefaultRouter()
router.register(r'anuncios', AnuncioViewSet)
router.register(r'imoveis', ImovelViewSet)
router.register(r'reservas', ReservasViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
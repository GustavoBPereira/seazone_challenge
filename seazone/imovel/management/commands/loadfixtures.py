from django.core.management import call_command
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Load fixtures in correct order'

    def handle(self, *args, **kwargs):
        call_command('loaddata', 'fixtures/imovel.json')
        call_command('loaddata', 'fixtures/anuncio.json')
        call_command('loaddata', 'fixtures/reserva.json')
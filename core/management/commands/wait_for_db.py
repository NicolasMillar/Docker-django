from django.core.management import BaseCommand
from django.db import connections
from django.db.utils import OperationalError
import time

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Waiting for the dattabase...')
        conn = None

        while not conn:
            try:
                conn = connections['default']
            except OperationalError:
                self.stdout.write('Database no alcanzada, esperando por 1 segundo ...')
                time.sleep(1) 
        self.stdout.write('¡Conectado a la base de datos!')
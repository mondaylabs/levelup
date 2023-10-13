from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.db import transaction


class Command(BaseCommand):
    help = 'Loads default fixtures'

    @transaction.atomic
    def handle(self, *args, **options):
        fixtures = settings.DEFAULT_FIXTURES or []
        call_command('loaddata', *fixtures)

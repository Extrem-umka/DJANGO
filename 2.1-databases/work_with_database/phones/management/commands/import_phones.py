import csv
from django.template.defaultfilters import slugify
from django.core.management.base import BaseCommand
from phones.models import Phone
from django.http import HttpResponse
from django.conf import settings

class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

            for phone in phones:
                ph = Phone.objects.create(
                    id=phone['id'], name=phone['name'], price=phone['price'], image=phone['image'],
                    release_date=phone['release_date'], lte_exists=phone['lte_exists'], slug=phone['name']
                )



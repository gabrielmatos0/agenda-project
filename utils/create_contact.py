import os
import sys
import django

from django.conf import settings

DJANGO_BASE_DIR = ...
NUMBER_OF_OBJECTS = 1000

sys.path.append(DJANGO_BASE_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'
settings.USB_TZ = False

django.setup()

if __name__ == '__main__':
    import faker

    from contact.models import Category, Contact

    # Contact.objects.all().delete()
    # Category.objects.all().delete()

    faker = faker.Faker('pt_BR')
    categories = []

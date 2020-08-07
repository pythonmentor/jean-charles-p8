from django.core.management.base import BaseCommand, CommandError
from user import models as usr
from product import models as prd


class Command(BaseCommand):
    help = 'Puge the database via Django models'


    def  handle(self, *args, **options):
        """ lance la purge sur produits et categories """
        prd.Product.objects.all().delete()
        prd.Category.objects.all().delete()
        pass




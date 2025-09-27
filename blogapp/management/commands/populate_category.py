from blogapp.models import Category
from django.core.management.base import BaseCommand



class Command(BaseCommand):
    help='This is command insert the Category data'

    def handle(self, *args, **kwargs):

        #deleting existing data from DB
        Category.objects.all().delete()

        Categories=['Sports' , 'Technology' , 'Finance' , 'Politics' , 'HelthCare']

        for Categorie_name in  Categories:
            Category.objects.create(name=Categorie_name)

        self.stdout.write(self.style.SUCCESS("Insertion Completed..."))
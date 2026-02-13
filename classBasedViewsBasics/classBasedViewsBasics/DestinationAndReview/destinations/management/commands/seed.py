from django.core.management.base import BaseCommand
from destinations.models import Destination
from reviews.models import Review
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Seeds the database with destinations and reviews.'

    def handle(self, *args, **options):
        self.stdout.write('Seeding database...')
        
        faker = Faker()

        # Clear existing data
        Destination.objects.all().delete()
        Review.objects.all().delete()

        # Create 10 destinations
        for _ in range(10):
            destination = Destination.objects.create(
                name=faker.city(),
                description=faker.text(),
                country=faker.country()
            )

            # Create a review for each destination
            Review.objects.create(
                author=faker.name(),
                body=faker.text(),
                rating=random.uniform(1, 5),
                destination=destination,
                is_published=True
            )

        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))
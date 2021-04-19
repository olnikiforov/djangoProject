"""Generation books with categories."""
from django.core.management.base import BaseCommand
from faker import Faker
from main.models import Author, Book, Category


class Command(BaseCommand):
    """Command Class."""

    def handle(self, *args, **kwargs):
        """Handle func."""
        Categories = ['Art&Music',
                      'Biographies',
                      'Business',
                      'Comics',
                      'Tech',
                      'Cooking',
                      'Edu',
                      'Enterteiment',
                      'Health',
                      'Fitness',
                      'History',
                      'Hobbies',
                      'Garden',
                      'Garden',
                      'Horror',
                      'Kids',
                      'Sports',
                      'Western',
                      'Religion',
                      'Travel',
                      'Teen']

        fake = Faker()

        for _ in range(50):
            Author(name=fake.name(), last_name=fake.name(), email=fake.email()).save()

        for category in Categories:
            Category(name=category).save()

        for _ in range(300):
            author = Author.objects.all().order_by('?').last()
            category = Category.objects.all().order_by('?').last()
            Book(title=fake.text(max_nb_chars=20).replace('.', ''), author=author, category=category).save()

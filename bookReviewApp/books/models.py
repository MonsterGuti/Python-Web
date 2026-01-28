from django.db import models
from django.template.defaultfilters import slugify


class Book(models.Model):
    class GenreChoices(models.TextChoices):
        FICTION = "FICTION", "FICTION"
        NON_FICTION = "Non-Fiction", "Non-Fiction"
        FANTASY = "Fantasy", "Fantasy"
        SCIENCE = "Science", "Science"
        HISTORY = "History", "History"
        BIOGRAPHY = "Biography", "Biography"

    title = models.CharField(
        max_length=200,
        unique=True,
    )

    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
    )

    isbn = models.CharField(
        max_length=12,
        unique=True,
    )

    genre = models.CharField(
        max_length=20,
        choices=GenreChoices.choices,
    )

    publishing_date = models.DateField()

    description = models.TextField()

    image_url = models.URLField(blank=True)

    slug = models.SlugField(
        unique=True,
        blank=True,
        max_length=100,
    )

    updated_at = models.DateTimeField(auto_now=True)

    pages = models.PositiveIntegerField(null=True, blank=True)

    publisher = models.CharField(max_length=150, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.title}-{self.publisher}')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

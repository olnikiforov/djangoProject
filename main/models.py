"""Models for site."""
from django.db import models
from django.utils.timezone import now


# Create your models here.
class Author(models.Model):
    """Class Author."""

    class Meta:
        """Meta class."""

        db_table = "tbl_users"
        verbose_name = "Author"
        verbose_name_plural = "Authors"
    name = models.CharField("Author name", max_length=100)
    email = models.EmailField("Email", max_length=50)

    def __str__(self):
        """Print method."""
        return self.name


class Subscriber(models.Model):
    """Class Subsriber."""

    class Meta:
        """Meta class."""

        unique_together = ['email_to', 'author_id']
        db_table = "tbl_subscribers"
        verbose_name = "Subscriber"
        verbose_name_plural = "Subsribers"

    email_to = models.EmailField("Email", max_length=100)
    author_id = models.ForeignKey("Author", on_delete=models.CASCADE)

    def __str__(self):
        """Print method."""
        return self.email_to


class Post(models.Model):
    """Class for Post."""

    class Meta:
        """Meta class."""

        db_table = "  tbl_posts"
        verbose_name = "Post"
        verbose_name_plural = "Posts"
    title = models.CharField("Post title", max_length=100)
    description = models.TextField("Post description", max_length=100)
    content = models.TextField("Post content")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(default=now)

    def __str__(self):
        """Print method."""
        return self.title

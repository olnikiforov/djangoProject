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
    last_name = models.CharField("Author surname", max_length=100, blank=True)
    email = models.EmailField("Email", max_length=50)

    def __str__(self):
        """Print method."""
        return self.name

    def get_full_name(self):
        """Make full name."""
        return f'{self.name} {self.last_name}'

    @property
    def full_name(self):
        """Print full name."""
        return f'{self.name} {self.last_name}'


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


class Logger(models.Model):
    """Logger class."""

    class Meta:
        """Meta class."""

        db_table = "tb_loggers"

    utm = models.CharField("UTM ", max_length=50)
    time_execution = models.CharField("Time execute ", max_length=70)
    created = models.DateTimeField(auto_now_add=True)
    path = models.CharField("Path", max_length=70)
    user_ip = models.CharField("User IP", max_length=20)

    def __str__(self):
        """Print method."""
        return self.utm


class Comments(models.Model):
    """Set comments model in database."""

    class Meta:
        """Special Meta class to define database and post ordering by created."""

        db_table = "tb_comments"
        ordering = ("created",)

    post = models.ForeignKey("Post", related_name="comments", on_delete=models.CASCADE)
    body = models.TextField("Comment")
    subs_id = models.ForeignKey("Subscriber", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(default=now)
    activate = models.BooleanField(default=True)

    def __str__(self):
        """Set method of printing."""
        return "Comment by {} on {}".format(self.subs_id, self.post)


class Book(models.Model):
    """Class books."""

    title = models.CharField('Title', max_length=60)
    author = models.ForeignKey('Author', models.CASCADE, related_name='books')
    category = models.ForeignKey('Category', models.CASCADE, related_name='books')

    def __str__(self):
        """Print method."""
        return self.title


class Category(models.Model):
    """Class Category."""

    name = models.CharField("Category name: ", max_length=60)

    def __str__(self):
        """Print method."""
        return self.name

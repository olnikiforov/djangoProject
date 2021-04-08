"""Post Service."""
from main.models import Post


def post_all():
    """Take all from class Post."""
    objects_all = Post.objects.all()
    return objects_all

"""Post Service."""
from main.models import Post


def post_all():
    """Take all from class Post."""
    objects_all = Post.objects.all()
    return objects_all


def post_find(post_id: int) -> Post:
    """Find post."""
    return Post.objects.get(id=post_id)

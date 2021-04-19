"""Post Service."""
from main.forms import CommentsForm
from main.models import Post


def post_all():
    """Take all from class Post."""
    objects_all = Post.objects.all()
    return objects_all


def post_find(post_id: int) -> Post:
    """Find post."""
    return Post.objects.get(id=post_id)


def comment_method(post, request):
    """Show comments."""
    comments = post.comments.filter(activate=True)
    if request.method == 'POST':
        comment_form = CommentsForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentsForm()
    return comment_form, comments

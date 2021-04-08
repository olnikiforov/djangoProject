"""All wiews of site."""
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from main.forms import PostForm, SubscriberForm
from main.models import Author, Post
from main.notify_service import notify
from main.post_service import post_all
from main.subscribe_service import subscribe


def index(request):
    """Homepage."""
    return render(request, "main/index.html", {'title': 'homepage'})


def about(request):
    """About page."""
    return render(request, "main/about.html", {'title': 'about'})


def posts(request):
    """Show all posts."""
    _posts = Post.objects.all()
    return render(request, "main/posts.html", {'title': "Posts", "posts": _posts})


def post_create(request):
    """Create posts."""
    errors = ''
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            errors = "Cannot save the post"
    else:
        form = PostForm()
    context = {
        "form": form,
        "errors": errors
    }
    return render(request, "main/post_create.html", context=context)


def post_api(request):
    """Post api show."""
    posts = post_all()
    data = [dict(title=post.title, description=post.description, content=post.content) for post in posts]
    return JsonResponse(data, safe=False)


def subscribe_notify(author_id, email_to):
    """Subscribe and Notify."""
    if subscribe(author_id, email_to):
        notify(email_to)
        return True
    return False


def posts_subscribe(request):
    """Post Subscribe with ID."""
    errors = ''
    if request.method == "POST":
        form = SubscriberForm(request.POST)
        if form.is_valid():
            author_id = request.POST['author_id']
            email_to = request.POST['email_to']
            subscribe_success = subscribe_notify(author_id, email_to)
            if subscribe_success:
                return redirect("posts")
            else:
                errors = "Вы уже подписаны на этого автора."
        else:
            errors = "Подписка не была осуществлена."
    else:
        form = SubscriberForm()
    context = {"form": form, "errors": errors}
    return render(request, "main/subscriber.html", context=context)


def api_subscribe(request):
    """Route Subscribers API."""
    author_id = request.GET["author_id"]
    email_to = request.GET["email_to "]
    get_object_or_404(Author, pk=author_id)
    subscribe_notify(author_id, email_to)
    data = {"author_id": author_id}
    return JsonResponse(data, safe=False)

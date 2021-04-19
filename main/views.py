"""All wiews of site."""
from time import time

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from faker import Faker
from main.forms import PostForm, SubscriberForm
from main.models import Author, Post, Subscriber
from main.notify_service import notify
from main.post_service import comment_method, post_all, post_find
from main.subscribe_service import subscribe
from main.tasks import notify_on_subscription, notify_subs


def index(request):
    """Homepage."""
    return render(request, "main/index.html", {'title': 'homepage'})


def about(request):
    """About page."""
    return render(request, "main/about.html", {'title': 'about'})


def posts(request):
    """Show all posts."""
    return render(request, "main/posts.html", {'title': "Posts", "posts": post_all()})


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


def post_update(request, post_id):
    """Update posts."""
    err = ""
    pst = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        form = PostForm(instance=pst, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("posts")
        else:
            err = "Cannot update."
    else:
        form = PostForm(instance=pst)
    context = {
        "form": form,
        "err": err
    }
    return render(request, "main/post_update.html", context=context)


def post_show(request, post_id):
    """Show post by ID."""
    pst = post_find(post_id)
    comment_form, comments = comment_method(pst, request)
    return render(request, "main/post_show.html",
                  {"title": pst.title, "pst": pst, "comments": comments, "comment_form": comment_form})


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


def author_subscribe(request):
    """Subscribe on Author."""
    errors = ''
    sub_success = False
    email_to = request.POST.get('email_to')
    if request.method == "POST":
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            sub_success = True
        else:
            errors = form.errors
    else:
        form = SubscriberForm()

    if sub_success:
        notify_on_subscription.delay(email_to)
        return redirect("author_subscribers_all")

    context = {"form": form, "errors": errors}
    return render(request, "main/subscriber.html", context=context)


def authors_new(request):
    """Generate author."""
    fake = Faker()
    Author(name=fake.name(), email=fake.email()).save()
    return redirect("authors_all")


def author_subscribers_all(request):
    """Show all subscribers."""
    allsubs = Subscriber.objects.all()
    return render(request, "main/subscribers_all.html", {"title": "All Subscrivers", "subscribers_all": allsubs})


def authors_all(request):
    """Show a list of authors."""
    allauthors = Author.objects.all()
    return render(request, "main/authors_all.html", {"title": "Authors", "authors": allauthors})


def subscribers_notify(request):
    """Notify all subscribers."""
    st = time()
    notify_subs.delay()
    exc_t = time() - st
    print('Time of execution:', exc_t)
    return redirect('homepage')



def api_subscribe(request):
    """Route Subscribers API."""
    author_id = request.GET["author_id"]
    email_to = request.GET["email_to "]
    get_object_or_404(Author, pk=author_id)
    subscribe_notify(author_id, email_to)
    data = {"author_id": author_id}
    return JsonResponse(data, safe=False)


def api_authors_new(request):
    """Generate fake author by Faker for API in Json Format."""
    fake = Faker()
    Author(name=fake.name(), email=fake.email()).save()
    authors = Author.objects.all().values("name", "email")
    return JsonResponse(list(authors), safe=False)

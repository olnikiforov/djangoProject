"""Admin of Django."""
from account.models import Ava, Profile, User
from django.contrib import admin
from main.models import Author, Comments, Logger, Post, Subscriber


# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    """Sort comments in admin view."""

    list_display = ("subs_id", "body", "post", "created", "activate")
    list_filter = ("activate", "created", "updated")
    search_fields = ("subs_id", "body")

class UserAdmin(admin.ModelAdmin):
    """User admin class"""

    list_display = ("email", "first_name")
    list_filter = ("is_active", "is_staff",)
    readonly_fields = ("confirmation_token", "is_active", "date_joined", "last_login")


admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Subscriber)
admin.site.register(Logger)
admin.site.register(Comments, CommentAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Ava)
admin.site.register(Profile)

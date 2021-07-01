"""Views of account."""
from account.models import User
from django.contrib import messages
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, View

from .forms import UserRegistrationForm
# Create your views here.


class MyProfile(LoginRequiredMixin, UpdateView):
    """Class Profile."""

    queryset = User.objects.filter(is_active=True)
    fields = ("first_name", "last_name",)
    success_url = reverse_lazy("homepage")

    def get_object(self, queryset=None):
        """Get object."""
        return self.request.user


class SignUpView(CreateView):
    """Sign up."""

    model = User
    form_class = UserRegistrationForm
    template_name = 'account/user_sign_up.html'
    success_url = reverse_lazy('home_page')


class ActivateUserView(View):
    """Activate user."""

    def get(self, request, confirmation_token):
        """Get method."""
        user = get_object_or_404(User, confirmation_token=confirmation_token)
        user.is_active = True
        user.save(update_fields=('is_active',))
        return redirect("homepage")


def change_password(request):
    """Change password."""
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password saved!')
            return redirect('homepage')
        else:
            messages.error(request, 'Error!')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'account/user_change_password.html', {
        'form': form
    })


def logout(request):
    """Logout."""
    auth_logout(request)
    return redirect("homepage")

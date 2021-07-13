"""Views of account."""
from account.forms import AvaForm, ProfileForm
from account.models import Ava, Profile, User
from django.contrib import messages
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, View

from .forms import UserRegistrationForm

# Create your views here.


class MyProfile(LoginRequiredMixin, UpdateView):
    """Class Profile."""

    form_class = ProfileForm
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


class ShowProfilePageView(DetailView):
    """Show profile class."""

    model = Profile
    template_name = 'account/user_profile.html'
    queryset = Ava.objects.all()

    def get_context_data(self, *args, **kwargs):
        """Get data method."""
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context

    def get_object(self, queryset=None):
        """Get user from request."""
        return self.request.user


class ActivateUserView(View):
    """Activate user."""

    @staticmethod
    def get(request, confirmation_token):
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


class AvaCreateView(LoginRequiredMixin, CreateView):
    """Ava create view."""

    model = Ava
    form_class = AvaForm
    success_url = reverse_lazy("homepage")

    def get_form_kwargs(self):
        """Get from kwargs method."""
        super_kwargs = super().get_form_kwargs()
        super_kwargs["request"] = self.request
        return super_kwargs


class AvaListView(LoginRequiredMixin, ListView):
    """Ava list view."""

    queryset = Ava.objects.all()

    def get_queryset(self):
        """Get queryset method."""
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

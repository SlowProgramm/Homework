from django.shortcuts import render
from django.contrib.auth.models import User
from app.models import Songs
from django.views.generic import CreateView, View, DetailView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView

# from django.contrib.auth.forms import AuthenticationForm - Для красивой формы
from users.forms import RegistrationForm


class RegistrationView(CreateView):
    model = User
    # fields = ('__all__')
    form_class = RegistrationForm
    success_url = '/'
    template_name = 'users/user_form.html'


class UserLoginView(LoginView):
    template_name = 'users/login_form.html'
    pass


class UserLogoutView(LogoutView):
    # В settings я указал url при переходе
    pass


class UserCabinet(DetailView):
    model = User
    template_name = 'users/user_detail.html'

    def get_queryset(self):
        return super().get_queryset().filter(id=self.request.user.id)


class UserProfile(TemplateView):
    template_name = 'users/user_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.request.user

        context['user_songs'] = Songs.objects.filter(author=User.objects.get(username=self.request.user.username))
        return context







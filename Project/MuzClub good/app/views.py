from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, DeleteView, View
from app.models import Category, Songs
from random import random
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect, StreamingHttpResponse
from users.forms import SongCreationForm
import os

from django.conf.urls.static import static
import mimetypes
from django.http.response import HttpResponse
# python manage.py runserver


def random_rating():  # Для собственного пользования
    return round(random() * 5, 1)


def main_page(request):
    if request.method == "GET":
        return render(request, 'hello.html')

    if request.method == "POST":
        print('SAAAAAAAAADDDDDDDDDDDDDDDDDDDDSSSSSSSSSSSSSS')
        return HttpResponseRedirect('/')


class GenreCreateView(LoginRequiredMixin, CreateView):
    fields = ('title',)
    model = Category
    success_url = reverse_lazy('genres')


class GenresListView(ListView):
    model = Category


class SongDetailView(DetailView):
    model = Songs


def Song_List(request):
    if request.method == "GET":
        object_list = Songs.objects.all()
        return render(request, 'app/songs_list.html', {'object_list': object_list})


class SongDeleteView(DeleteView):
    model = Songs
    success_url = reverse_lazy('songs')


def SongDelete(request, pk):
    if request.method == "GET":
        song = Songs.objects.get(id=pk)
        song.delete()
        return HttpResponseRedirect('/songs/')


@login_required
def SongCreate(request):
    if request.method == "GET":
        form = SongCreationForm()
        form_user = User.objects.get(username=request.user.username)
        return render(request, 'app/songs_form.html', {'form': form, 'form_user': form_user})
    if request.method == "POST":
        New_object = Songs(name=request.POST['name'], category=Category.objects.get(id=request.POST['category']),
                           author=User.objects.get(username=request.user.username),
                           image=request.FILES.get('image'), file=request.FILES.get('file'))
        new_file_name = New_object.name + '_' + New_object.author.username
        new_file_name = new_file_name.replace(' ', '_')
        New_object.file.name = new_file_name
        print(New_object)
        New_object.save()
        return HttpResponseRedirect('/songs/')


def LatestSongs(request):
    return render(request, 'app/latest.html')

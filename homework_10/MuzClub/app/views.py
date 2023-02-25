from django.shortcuts import render
from django.views.generic import ListView, DetailView
from app.models import Category, Song, Author
from random import random


def random_rating(): # Для собственного пользования
    return round(random()*5, 1)


def main_page(request):
    return render(request, 'hello.html')


class SongListView(ListView):
    model = Song

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['help_text'] = 'Помогающий текст'
        return context


class SongDetailView(DetailView):
    model = Song

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from app.models import Category, Songs, Author


def main_page(request):
    return render(request, 'hello.html')


class SongListView(ListView):
    model = Songs


class SongDetailView(DetailView):
    model = Songs

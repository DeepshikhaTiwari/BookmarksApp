from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import bookmark


def index(request):
    return render(request, 'index.html')


class BookmarkDetailView(generic.DetailView):
    model = bookmark
    paginate_by = 4


class BookmarkListView(generic.ListView):
    model = bookmark
    paginate_by = 4


class CreateBookmark(generic.CreateView):
    model = bookmark
    fields = {'url', 'name', 'description', 'tag'}


class UpdateBookmark(generic.UpdateView):
    model = bookmark
    fields = '__all__'
    context_object_name = 'bookmarks'


class DeleteBookmark(generic.DeleteView):
    model = bookmark
    template_name = 'bookmarks/bookmark_delete.html'
    success_url = reverse_lazy('bookmark')

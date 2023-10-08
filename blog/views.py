# blog/views.py
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy

from .models import Post #Class created in App/models


class BlogListView(ListView):
    model = Post
    template_name = "home.html"

class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

class BlogCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ["title", "author", "body","color"]

class BlogUpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ["title", "author", "body","color"]

class BlogDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    fields = ["title", "author", "body","color"]
    success_url = reverse_lazy("home")



from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import CommentModel

# Create your views here.
class NewComment(CreateView):
    model = CommentModel
    fields = "__all__"

class CommentList(ListView):
    model = CommentModel
    template_name = "detailBlog.html"
    context_object_name = 'comments'
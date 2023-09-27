from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Blog
from .forms import BlogCreateForm


class HomeView(ListView, LoginRequiredMixin):
    login_url = '/account/login/'
    template_name = 'homepage.html'
    model = Blog
    context_object_name = 'items'

class BlogCreateView(View, LoginRequiredMixin):
    login_url = '/account/login/'

    def get(self,request, *args, **kwargs):
        form = BlogCreateForm()
        return render(request, 'createBlog.html',{'form': form})

    def post(self,request, *args, **kwargs):
        form = BlogCreateForm(request.POST)
        if form.is_valid():
            data = form.clean()
            data.update(author_id = request.user.id)
            Blog.objects.create(**data)
            return redirect('blog.home')
        return render(request, 'createBlog.html', {'form': form})
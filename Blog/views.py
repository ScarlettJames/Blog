from django.shortcuts import render, redirect, resolve_url
from django.views.generic import ListView, View, DetailView
from django.views.generic.edit import ModelFormMixin
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
    
class BlogDetailView(ModelFormMixin, DetailView, LoginRequiredMixin):
    login_url = '/account/login/'
    template_name = 'updateBlog.html'
    success_url = '/blog/home'
    model = Blog
    form_class = BlogCreateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        init_obj = self.get_object()
        context['form'] = BlogCreateForm(instance=init_obj)
        return context
    
    def post(self, request, *args, **kwargs):
        blog_obj = self.get_object()
        form = BlogCreateForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            body = form.cleaned_data['body']
            blog_obj.title, blog_obj.body = title, body
            blog_obj.save()
            return redirect('blog.home')
        return redirect('blog.update')
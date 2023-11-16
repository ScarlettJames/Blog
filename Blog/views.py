from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, View, DetailView, UpdateView, DeleteView
from .models import Blog
from .forms import BlogCreateForm


class HomeView(ListView):
    template_name = 'homepage.html'
    model = Blog
    context_object_name = 'items'
    paginate_by = 2
    ordering = ["-post_created"]

class BlogCreateView(View):

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
    
class BlogUpdateView(UpdateView):
    template_name = 'updateBlog.html'
    success_url = '/blog/home'
    model = Blog
    form_class = BlogCreateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        init_obj = self.get_object()
        context['form'] = BlogCreateForm(instance=init_obj)
        return context
    
class BlogDetailView(DetailView):
    template_name = "detailBlog.html"
    model = Blog
    context_object_name = 'item'

class BlogDeleteView(DeleteView):
    model = Blog
    context_object_name = "item"
    success_url = reverse_lazy('blog.home')
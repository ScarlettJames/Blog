from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import CommentModel
from django.contrib.auth.models import User
from Blog.models import Blog
from django.http import JsonResponse
from json import dumps

# Create your views here.
class NewComment(CreateView):
    model = CommentModel
    fields = "__all__"

    def post(self, request, *args, **kwargs):
        data = dict(request.POST)
        comment = data['comment'][0]
        user = User.objects.get(pk = int(data['author'][0]))
        post = Blog.objects.get(pk = int(data['post'][0]))
        modelCreated = self.model.objects.create(author = user, post = post, comment = comment)
        return JsonResponse({'success': True})
    
class CommentList(ListView):
    template_name = 'commentlist.html'
    model = CommentModel
    context_object_name = 'comments'
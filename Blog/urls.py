from django.urls import path
from .views import HomeView, BlogCreateView, BlogUpdateView, BlogDetailView, BlogDeleteView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('home/', HomeView.as_view(), name='blog.home'),
    path('new-blog/', login_required(BlogCreateView.as_view()), name='blog.new'),
    path('update-blog/<pk>/', login_required(BlogUpdateView.as_view()), name='blog.update'),
    path('detail-blog/<pk>/', login_required(BlogDetailView.as_view()), name='blog.detail'),
    path('delete-blog/<pk>/', login_required(BlogDeleteView.as_view()), name='blog.delete')
]
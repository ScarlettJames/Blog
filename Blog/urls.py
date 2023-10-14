from django.urls import path
from .views import HomeView, BlogCreateView, BlogDetailView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('home/', HomeView.as_view(), name='blog.home'),
    path('new-blog/', login_required(BlogCreateView.as_view()), name='blog.new'),
    path('update-blog/<pk>/', login_required(BlogDetailView.as_view()), name='blog.update'),
]
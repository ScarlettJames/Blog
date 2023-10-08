from django.urls import path
from .views import HomeView, BlogCreateView, BlogDetailView

urlpatterns = [
    path('home/', HomeView.as_view(), name='blog.home'),
    path('new-blog/', BlogCreateView.as_view(), name='blog.new'),
    path('update-blog/<pk>/', BlogDetailView.as_view(), name='blog.update'),
]
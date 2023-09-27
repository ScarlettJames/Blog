from django.urls import path
from .views import HomeView, BlogCreateView

urlpatterns = [
    path('home/', HomeView.as_view(), name='blog.home'),
    path('new-blog/', BlogCreateView.as_view(), name='blog.new'),
]
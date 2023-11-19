from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import NewComment

urlpatterns = [
    path('new', NewComment.as_view(), name='comment.new'),
]
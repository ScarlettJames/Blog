from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.decorators.clickjacking import xframe_options_sameorigin
from .views import NewComment, CommentList

urlpatterns = [
    path('new', NewComment.as_view(), name='comment.new'),
    path('commentlist', xframe_options_sameorigin(CommentList.as_view()), name='comment.list'),
]
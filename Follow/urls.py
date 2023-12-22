from django.urls import path, include
from .views import AddFollowerView, GetFollowerView

urlpatterns = [
    path('follow/', AddFollowerView.as_view(), name="user.addfollower"),
    path('following/', AddFollowerView.as_view(), name="user.getfollower"),
]
from django.urls import path
from .views import RegisterView, LoginView, LogoutView, ProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='account.register'),
    path('login/', LoginView.as_view(), name='account.login'),
    path('logout/', LogoutView.as_view(), name='account.logout'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='account.profile')
]

from django.http import JsonResponse
from django.views.generic import CreateView, View
from .models import UserFollowing

# Create your views here.
class AddFollowerView(View):

    def post(self, request, *args, **kwargs): 
        print(request.POST)
        return JsonResponse({'success': True})
        
class GetFollowerView(View):
    
    def get(self, request, *args, **kwargs):...
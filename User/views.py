from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Profile
from django.views.generic import View, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserForm, LoginForm
from django.contrib.messages import success, error
from django.contrib.auth.hashers import check_password
from django.contrib.auth import login,logout

class RegisterView(View):
    
    def get(self,request, *args, **kwargs):
        return render(request, 'register.html', {'form': UserForm})
    
    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['passwordOne']
            confirm_password = form.cleaned_data['passwordTwo']
            if password == confirm_password:
                User.objects.create_user(username,email,password)
                success(request, f'Success! {username} is created.', fail_silently=True)
                return render(request,'login.html')
            error(request, 'Password doesn\'t match. Try again!')
            return redirect('account.register')
        
class LoginView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'login.html', {'form': LoginForm})
    
    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(email=email)
            except:
                user = None
            if user != None and check_password(password, user.password):
                login(request, user)
                return redirect('blog.home')
            error(request, 'Something went wrong. Try again!', fail_silently=True)
            return redirect('account.login')
        
class ProfileView(UpdateView, LoginRequiredMixin):
    model = Profile
    fields = ['image']
    template_name = 'updateProfile.html'
    success_url = '/blog/home'

    def get(self, request, *args, **kwargs):
        profile = self.model.objects.get(user_id = kwargs["pk"])
        context = {'profile' : profile}
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        email = request.POST.get('email')
        User.objects.update(username=username, email=email)
        return super().post(request, *args, **kwargs)

class LogoutView(View):
    
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('account.login')
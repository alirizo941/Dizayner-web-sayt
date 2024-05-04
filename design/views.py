from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

class HomeView(View):
    def get(self,request):
        return render(request,'home.html')


class GalleryView(View):
    def get(self,request):
        return render(request,'GALLERY.html')
    
class AboutView(View):
    def get(self,request):
        return render(request,'ABOUT-US.html')
    
class ProjectsView(View):
    def get(self,request):
        return render(request,'Projects.html')
    

class RegisterView(View):
    def get(self, request):
        return render(request, "register.html")

    def post(self, request):
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')

            
        user = User.objects.create_user(
            username=username,
            first_name=firstname,
            last_name=lastname,
            email=email,
            password=password,
        )

        return redirect('login') 

class LoginView(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        check = AuthenticationForm(data=request.POST)

        if check.is_valid():
            user = check.get_user()
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')
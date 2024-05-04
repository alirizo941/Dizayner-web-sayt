from django.urls import path
from .views import HomeView,GalleryView,AboutView,ProjectsView,LoginView,RegisterView

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('gallery/',GalleryView.as_view(),name='gallery'),
    path('about/',AboutView.as_view(),name='about'),
    path('projects/',ProjectsView.as_view(),name='projects'),
    path('login/',LoginView.as_view(),name='login'),
    path('register/',RegisterView.as_view(),name='register'),

]
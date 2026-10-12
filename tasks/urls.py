from django.urls import path
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(
        template_name='login.html',
        next_page='dashboard',
        redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('tasks/add/', views.add_task, name='add_task'),
    path('tasks/<int:pk>/toggle/', views.toggle_task, name='toggle_task'),
    path('tasks/<int:pk>/delete/', views.delete_task, name='delete_task'),
    path('accounts/profile/', RedirectView.as_view(pattern_name='dashboard')),
]
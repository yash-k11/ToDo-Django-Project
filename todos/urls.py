from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    
    # This is your existing custom login
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    
    # Add this so Django's default /accounts/login/ works too
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html')),
    
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.todo_list, name='todo_list'),
    path('create/', views.todo_create, name='todo_create'),
    path('edit/<int:pk>/', views.todo_edit, name='todo_edit'),
    path('delete/<int:pk>/', views.todo_delete, name='todo_delete'),
]

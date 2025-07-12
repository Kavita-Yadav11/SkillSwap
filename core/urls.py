from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('skills/', views.manage_skills, name='manage_skills'),
    path('swap/', views.swap_requests, name='swap_requests'),
    path('swap/accept/<int:swap_id>/', views.accept_swap, name='accept_swap'),
    path('swap/reject/<int:swap_id>/', views.reject_swap, name='reject_swap'),
    path('swap/cancel/<int:swap_id>/', views.cancel_swap, name='cancel_swap'),
    path('swap/delete/<int:swap_id>/', views.delete_swap, name='delete_swap'),
]

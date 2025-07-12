from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('skills/', views.manage_skills, name='manage_skills'),
    path('skills/delete/<int:skill_id>/', views.delete_skill, name='delete_skill'),
    path('swap/', views.swap_requests, name='swap_requests'),
    path('swap/accept/<int:request_id>/', views.accept_request, name='accept_request'),
    path('swap/reject/<int:request_id>/', views.reject_request, name='reject_request'),
    path('swap/cancel/<int:request_id>/', views.cancel_request, name='cancel_request'),
]
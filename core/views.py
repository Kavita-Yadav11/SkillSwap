from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, SkillForm, SwapRequestForm
from .models import User, Skill, SwapRequest
from django.contrib import messages

def home(request):
    if request.user.is_authenticated:
        # Get user's skills count
        user_skills_count = Skill.objects.filter(user=request.user).count()
        
        # Get incoming and outgoing requests counts
        incoming_requests_count = SwapRequest.objects.filter(to_user=request.user, status='pending').count()
        outgoing_requests_count = SwapRequest.objects.filter(from_user=request.user).count()
        
        # Get available users (public, not banned, not the current user)
        users = User.objects.filter(
            is_public=True, 
            is_banned=False
        ).exclude(id=request.user.id)
        
        available_users_count = users.count()
        
        context = {
            'user_skills_count': user_skills_count,
            'incoming_requests_count': incoming_requests_count,
            'outgoing_requests_count': outgoing_requests_count,
            'available_users_count': available_users_count,
            'users': users,
        }
    else:
        context = {}
    
    return render(request, 'core/home.html', context)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f"Account created successfully! Welcome to SkillSwap, {user.username}!")
            return redirect('login')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = RegisterForm()
    return render(request, 'core/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'core/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, "You have been successfully logged out.")
    return redirect('home')

@login_required
def profile(request):
    # Get user's skills
    offered_skills = Skill.objects.filter(user=request.user, type='offered')
    wanted_skills = Skill.objects.filter(user=request.user, type='wanted')
    
    context = {
        'user': request.user,
        'offered_skills': offered_skills,
        'wanted_skills': wanted_skills,
    }
    return render(request, 'core/profile.html', context)

@login_required
def manage_skills(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.user = request.user
            skill.save()
            messages.success(request, f"Skill '{skill.skill_name}' added successfully!")
            return redirect('manage_skills')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = SkillForm()
    
    skills = Skill.objects.filter(user=request.user)
    return render(request, 'core/skills.html', {'form': form, 'skills': skills})

@login_required
def swap_requests(request):
    if request.method == 'POST':
        form = SwapRequestForm(request.POST)
        if form.is_valid():
            swap = form.save(commit=False)
            swap.from_user = request.user
            swap.save()
            messages.success(request, f"Swap request sent to {swap.to_user.username}!")
            return redirect('swap_requests')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = SwapRequestForm()
        # Pre-fill to_user if provided in URL
        to_user_id = request.GET.get('to_user')
        if to_user_id:
            try:
                to_user = User.objects.get(id=to_user_id)
                form.initial['to_user'] = to_user
            except User.DoesNotExist:
                pass
    
    # Get available users for the form
    available_users = User.objects.filter(
        is_public=True, 
        is_banned=False
    ).exclude(id=request.user.id)
    
    incoming = SwapRequest.objects.filter(to_user=request.user).order_by('-id')
    outgoing = SwapRequest.objects.filter(from_user=request.user).order_by('-id')
    
    return render(request, 'core/swap_requests.html', {
        'form': form,
        'available_users': available_users,
        'incoming': incoming,
        'outgoing': outgoing
    })

@login_required
def accept_request(request, request_id):
    swap_request = get_object_or_404(SwapRequest, id=request_id, to_user=request.user)
    swap_request.status = 'accepted'
    swap_request.save()
    messages.success(request, f"Swap request accepted! You can now connect with {swap_request.from_user.username}.")
    return redirect('swap_requests')

@login_required
def reject_request(request, request_id):
    swap_request = get_object_or_404(SwapRequest, id=request_id, to_user=request.user)
    swap_request.status = 'rejected'
    swap_request.save()
    messages.success(request, f"Swap request rejected.")
    return redirect('swap_requests')

@login_required
def cancel_request(request, request_id):
    swap_request = get_object_or_404(SwapRequest, id=request_id, from_user=request.user)
    swap_request.status = 'cancelled'
    swap_request.save()
    messages.success(request, f"Swap request cancelled.")
    return redirect('swap_requests')

@login_required
def delete_skill(request, skill_id):
    skill = get_object_or_404(Skill, id=skill_id, user=request.user)
    skill_name = skill.skill_name
    skill.delete()
    messages.success(request, f"Skill '{skill_name}' deleted successfully!")
    return redirect('manage_skills')
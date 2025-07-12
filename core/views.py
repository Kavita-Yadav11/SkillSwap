from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, SkillForm, SwapRequestForm
from .models import User, Skill, SwapRequest
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect

def home(request):
    users = User.objects.filter(is_public=True, is_banned=False).exclude(id=request.user.id) if request.user.is_authenticated else []
    return render(request, 'core/home.html', {'users': users})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
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
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials")
    return render(request, 'core/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def profile(request):
    return render(request, 'core/profile.html', {'user': request.user})

@login_required
def manage_skills(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.user = request.user
            skill.save()
            return redirect('manage_skills')
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
            return redirect('swap_requests')
    else:
        form = SwapRequestForm()
    incoming = SwapRequest.objects.filter(to_user=request.user)
    outgoing = SwapRequest.objects.filter(from_user=request.user)
    return render(request, 'core/swap_requests.html', {
        'form': form,
        'incoming': incoming,
        'outgoing': outgoing
    })

@login_required
def accept_swap(request, swap_id):
    swap = get_object_or_404(SwapRequest, id=swap_id, to_user=request.user)
    if request.method == 'POST' and swap.status == 'pending':
        swap.status = 'accepted'
        swap.save()
    return HttpResponseRedirect(reverse('swap_requests'))

@login_required
def reject_swap(request, swap_id):
    swap = get_object_or_404(SwapRequest, id=swap_id, to_user=request.user)
    if request.method == 'POST' and swap.status == 'pending':
        swap.status = 'rejected'
        swap.save()
    return HttpResponseRedirect(reverse('swap_requests'))

@login_required
def cancel_swap(request, swap_id):
    swap = get_object_or_404(SwapRequest, id=swap_id, from_user=request.user)
    if request.method == 'POST' and swap.status == 'pending':
        swap.status = 'cancelled'
        swap.save()
        messages.success(request, "Swap request cancelled.")
    return redirect('swap_requests')

@login_required
def delete_swap(request, swap_id):
    swap = get_object_or_404(SwapRequest, id=swap_id, from_user=request.user)
    if request.method == 'POST' and swap.status != 'pending':
        swap.delete()
        messages.success(request, "Swap request deleted.")
    return redirect('swap_requests')
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Skill, SwapRequest

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'location', 'availability', 'password1', 'password2']

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['skill_name', 'type']

class SwapRequestForm(forms.ModelForm):
    class Meta:
        model = SwapRequest
        fields = ['to_user', 'skill_offered', 'skill_requested']

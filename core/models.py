from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    location = models.CharField(max_length=100, blank=True, null=True)
    is_public = models.BooleanField(default=True)
    is_banned = models.BooleanField(default=False)
    availability = models.CharField(max_length=100, blank=True, null=True)

class Skill(models.Model):
    SKILL_TYPE = (
        ('offered', 'Offered'),
        ('wanted', 'Wanted'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=SKILL_TYPE)

    def __str__(self):
        return f"{self.skill_name} ({self.type})"

class SwapRequest(models.Model):
    STATUS = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('cancelled', 'Cancelled'),
    )
    from_user = models.ForeignKey(User, related_name='sent_requests', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='received_requests', on_delete=models.CASCADE)
    skill_offered = models.CharField(max_length=100)
    skill_requested = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUS, default='pending')

class AdminLog(models.Model):
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

from django.contrib import admin
from .models import User, Skill, SwapRequest, AdminLog
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('location', 'is_public', 'is_banned', 'availability')}),
    )

admin.site.register(User, UserAdmin)
admin.site.register(Skill)
admin.site.register(SwapRequest)
admin.site.register(AdminLog)

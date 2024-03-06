from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import User
from .forms import ProfileForm


class AdminPanelUserDetailsLayout(UserAdmin):
    model = User
    list_display = ['username', 'email', 'gender', 'dob', 'age', 'profile_pic', 'date_joined']
    readonly_fields = ['last_login', 'date_joined']
    

    fieldsets = (
        ('Personal Info', {
            'fields': ('first_name', 'last_name', 'username', 'email', 'gender', 'dob', 'age', 'mobile_no',  'profile_pic',)
        }),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

admin.site.register(User, AdminPanelUserDetailsLayout)
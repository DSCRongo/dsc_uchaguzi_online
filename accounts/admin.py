from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
class UserTable(admin.ModelAdmin):
    list_display = ('email', 'gender', 'mobile_no', 'dob', 'age', 'profile_pic', 'date_updated')

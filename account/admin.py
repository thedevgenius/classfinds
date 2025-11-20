from django.contrib import admin
from .models import User
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('phone', 'is_staff', 'is_active')
    search_fields = ('phone',)
    list_filter = ('is_active',)
admin.site.register(User, UserAdmin)
from django.contrib import admin
from .models import Lead
# Register your models here.
class LeadAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'category', 'source', 'status', 'is_received', 'is_added', 'created_at')
    list_filter = ('source', 'status', 'is_received', 'is_added', 'created_at')
    search_fields = ('name', 'email', 'phone', 'category')
    ordering = ('-created_at',)
admin.site.register(Lead, LeadAdmin)
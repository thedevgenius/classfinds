from django.contrib import admin
from .models import Category, Business
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)

class BusinessAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'category', 'is_active', 'is_verified', 'is_featured')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'owner__username', 'biz_id')
    list_filter = ('is_active', 'is_verified', 'is_featured', 'category')

admin.site.register(Business, BusinessAdmin)
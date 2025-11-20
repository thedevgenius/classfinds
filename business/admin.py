from django.contrib import admin
from .models import Category, Business, State, City, Attribute, AttributeType
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

class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(State, StateAdmin)

class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'state')
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(City, CityAdmin)

class AttributeTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(AttributeType, AttributeTypeAdmin)

class AttributeAdmin(admin.ModelAdmin):
    list_display = ('value', 'type',)
    search_fields = ('type__name', 'value')
admin.site.register(Attribute, AttributeAdmin)
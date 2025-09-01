from django.contrib import admin
from .models import Project, Contact

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'technologies', 'created_at']
    list_filter = ['created_at', 'technologies']
    search_fields = ['title', 'description']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'email', 'message']
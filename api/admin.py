from django.contrib import admin

from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed')
    list_filter = ('completed', 'created', 'updated')
    search_fields = ('title', 'description', 'user__username')
    ordering = ('title', 'completed')



admin.site.register(Task, TaskAdmin)
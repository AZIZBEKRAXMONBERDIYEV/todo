from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed')
    list_filter = ('completed', 'created', 'updated')
    search_fields = ('title', 'description', 'user__username')
    ordering = ('title', 'completed')
    actions = ('mark_as_completed', 'mark_as_uncompleted')


    @admin.action(description='mark as completed')
    def mark_as_completed(self, request, queryset):
        queryset.update(completed=True)


    @admin.action(description='mark as uncompleted')
    def mark_as_uncompleted(self, request, queryset):
        queryset.update(completed=False)

admin.site.register(Task, TaskAdmin)
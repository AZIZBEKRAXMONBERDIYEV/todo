from django.contrib import admin

from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed', 'user_id', 'more_info')

    def user_id(self, obj):
        return obj.user.id

    def more_info(self, obj):
        return f"{obj.title} - {obj.description} - {obj.completed} - {obj.user.username}"


admin.site.register(Task, TaskAdmin)
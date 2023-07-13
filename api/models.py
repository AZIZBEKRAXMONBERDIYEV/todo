from django.db import models
from django.contrib.auth.models import User


# class Category(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories')
#     name = models.CharField(max_length=60)

#     def __str__(self) -> str:
#         return self.name
 
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=60)
    description = models.TextField(blank=True, default='')
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
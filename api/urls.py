from django.urls import path
from .views import TaskList, TaskDetail, Login
# from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('tasks/', TaskList.as_view()),
    path('tasks/<int:pk>/', TaskDetail.as_view()),
    path('login/', Login.as_view()),
    # path('login/', obtain_auth_token),
]
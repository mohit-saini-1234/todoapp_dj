from rest_framework.routers import DefaultRouter
from django.urls import path, include, re_path as url
from todo_task.views import TaskDetail , TaskList , TaskAssign ,TaskAssignGet , TaskInfo
from todo_task.roles import AssignRole
urlpatterns = [

    url(r'^task/$', TaskList.as_view()),
    url(r'^taskAssign/$', TaskAssign.as_view()),
    url(r'^taskAssignGet/$', TaskAssignGet.as_view()),
    path('taskview/<int:pk>/', TaskDetail.as_view()),
    path('role_add/<int:pk>/', AssignRole.as_view()),
    path('taskInfo/<int:pk>/', TaskInfo.as_view()),
]
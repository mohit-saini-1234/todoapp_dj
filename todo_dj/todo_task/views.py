from rest_framework.permissions import IsAuthenticated , IsAdminUser
from django.contrib.auth import authenticate
from django.contrib.auth.models import User ,  Permission
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import status
from todo_task.models import Task , TaskUser
from todo_task.serializer import TaskSerializer , TaskUserSerializer
from todo_dj.roles import SystemManager
from rolepermissions.checkers import has_permission

class TaskList(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self , request):
        user = self.request.user
        if has_permission(user,'Can view task'):
            todo_task = Task.objects.all()
            serializer = TaskSerializer(todo_task, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    def post(self , request):
        user = self.request.user
        if has_permission(user,'Can view task'):
            serializer = TaskSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
        
    
    
class TaskDetail(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, pk, format=None):
        user = self.request.user
        if has_permission(user,'Can view task'):
            log_task = Task.objects.get(pk=pk)
            serializer = TaskSerializer(log_task)
            return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    def put(self, request, pk, format=None):
        user = self.request.user
        if has_permission(user,'Can view task'):
            
            task = Task.objects.get(pk=pk)
            serializer = TaskSerializer(task,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=403)
    def delete(self, request, pk, format=None):
        user = self.request.user
        if has_permission(user,'Can view task'):
            
            task = Task.objects.get(pk=pk)
            task.delete()
            return Response({
                        'status': 'success',
                        'message': 'task deleted',
                    })
        return Response(status=status.HTTP_401_UNAUTHORIZED)
class TaskAssign(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self , request):
        user = self.request.user
        if has_permission(user,'Can add task'):
            if TaskUser.objects.filter(username=username).exists():
                return Response("username already exists")
            
            serializer = TaskUserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    def get(self , request):
        user = self.request.user 
        if has_permission(user,'Can view task'):
            todo_task = TaskUser.objects.all()
            serializer = TaskUserSerializer(todo_task, many=True)
            return Response(serializer.data)    
        return Response(status=status.HTTP_401_UNAUTHORIZED)

class TaskAssignGet(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self , request ,format=None ):
        email = request.user.email
        users_task = TaskUser.objects.filter(email=email)
        serializer = TaskUserSerializer(users_task, many=True)
        return Response(serializer.data)
class TaskInfo(APIView):
    def get(self, request, pk, format=None):
            
        log_task = Task.objects.get(pk=pk)
        serializer = TaskSerializer(log_task)
        return Response(serializer.data)
    
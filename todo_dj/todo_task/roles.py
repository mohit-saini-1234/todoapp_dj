from rolepermissions.roles import AbstractUserRole
from rolepermissions.permissions import register_object_checker
from rolepermissions.roles import assign_role
from rolepermissions.roles import remove_role
from django.contrib.auth.models import User ,  Permission
from rest_framework.response import Response
from rest_framework.decorators import APIView
from todo_dj.roles import SystemManager
from rest_framework.permissions import IsAuthenticated , IsAdminUser


class AssignRole(APIView):
    permission_classes = (IsAdminUser,)
    def get(self, request, pk, format=None):
        user = User.objects.get(pk=pk)
        assign_role(user, SystemManager)
        user.save()
        return  Response("Assign as Manager")

    
    def delete(self, request, pk, format=None):
        user = User.objects.get(pk=pk)
        remove_role(user, SystemManager)
        user.save()
        return  Response("remove as manager")
    
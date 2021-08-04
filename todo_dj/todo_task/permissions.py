from rolepermissions.permissions import register_object_checker
from todo_dj.roles import SystemManager
from rolepermissions.roles import assign_role
from rolepermissions.roles import remove_role
from rest_framework.permissions import IsAuthenticated , IsAdminUser
from rest_framework.decorators import APIView

#-----will work on it -----#
# @register_object_checker()
# def access_clinic(role, user, clinic):
#     if role == SystemManager:
#         return True

#     if user.clinic == clinic:
#         return True

#     return False


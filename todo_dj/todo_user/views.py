from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated , IsAdminUser
from django.contrib.auth import authenticate
from django.contrib.auth.models import User ,  Permission
from todo_user.serializer import UserSerializer , ChangePasswordSerializer,UpdateSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import generics
from rest_framework import status
from rolepermissions.checkers import has_permission




#from django.contrib.contenttypes.models import ContentType



class UserProfile(APIView):
    
    """
    Manager User Login and other things
    """

    permission_classes = (IsAuthenticated,)
    def get(self, request):
        ser = UserSerializer(request.user)
        print("@@@@@@@@@@@@-----@" ,ser)
        return Response(ser.data)
    
class UserAuth(APIView):
    
    def post(self, request):
        """
        login
        """
        user = authenticate(username=request.data.get(
            "username"), password=request.data.get("password"))
        if user is not None:
            # A backend authenticated the credentials
            try:
                token = Token.objects.get(user_id=user.id)
            except Token.DoesNotExist:
                token = Token.objects.create(user=user)
            return Response(token.key)
        else:
            # No backend authenticated the credentials
            return Response([], status=status.HTTP_401_UNAUTHORIZED)
        
        
        
        
# Create your views here.
class UserRegister(APIView):
    """
    Create user 
    """

    def post(self, request):
        user = User.objects.create_user(
            username=request.data.get("username"),
            email=request.data.get("email"),
            password=request.data.get("password"))
        user.save()

        if user is not None:
            token = Token.objects.create(user=user)
            print(token.key)
            print(user)
            return Response(token.key)
        else:
            return Response([], status=status.HTTP_400_BAD_REQUEST)
        
        
class ChangePasswordView(APIView):
        """
        An endpoint for changing password.
        """
        # serializer_class = ChangePasswordSerializer
        # print("##############--",serializer_class)
        # model = User
        permission_classes = [IsAuthenticated]

        # def get(self, queryset=None):
        #     obj = self.request.user
        #     #nn= request.user
        #     print("@@@@@@___@-----", obj)
        #     #print("@@@@@@___@-----", nn)
        #     return Response(str(obj))

        def post(self, request):
            log_username = self.request.user
            print("################@--",log_username)
            self.object = log_username
            print("***************||---",self.object)
            serializer = ChangePasswordSerializer(data=request.data)
            print("~~~~~~~~~~~~~~",serializer)

            if serializer.is_valid():
                # Check old password
                if not self.object.check_password(serializer.data.get("old_password")):
                    return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
                self.object.set_password(serializer.data.get("new_password"))
                self.object.save()
                return Response({
                        'status': 'success',
                        'code': status.HTTP_200_OK,
                        'message': 'Password updated successfully',
                    })

class DeleteUserView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        user = self.request.user
        if has_permission('Can delete user'):
        # self.obj = has_permission
            user.delete()
        #self.obj.save()
            return Response({
                        'status': 'success',
                        'code': status.HTTP_200_OK,
                        'message': 'delete updated successfully',
                    })
        return Response(status=403)

class UpdateUserView(APIView):
    permission_classes = [IsAuthenticated]
    def put(self, request):
        log_username = self.request.user
        serializer = UpdateSerializer(log_username,data=self.request.data)
        username=request.data.get("username"),
        if User.objects.filter(username=username).exists():
            return Response("username already exists")
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_204_NO_CONTENT)
            

from django.shortcuts import render
from django.contrib.auth import authenticate
from user.serializer import UserSerializered
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import status
from rolepermissions.checkers import has_permission
from user.models import NewUser
from django.contrib.auth import get_user_model 
from rest_framework.permissions import IsAuthenticated , IsAdminUser



class UserReg(APIView):
    """
    Create user 
    """

    def post(self, request):
        # user = self.request.data.get("username")
        #Serializer=User.objects.filter(request.data, many=True)
        # print("################---", user)
        #print("################---", Serializer)
        user3 = get_user_model() 
        print("**************",user3)
        ser= NewUser(
        role=request.data.get("role"),
        username=request.data.get("username"),
        first_name=request.data.get("first_name"),
        last_name=request.data.get("last_name"),
        email=request.data.get("email"),
        password=request.data.get("password"),
        phone_number=request.data.get("phone_number"),
        address=request.data.get("address"))
        
        username=request.data.get("username")
        email=request.data.get("email"),
        phone_number=request.data.get("phone_number"),
        role=request.data.get("role")
        # try:
        #     (User.objects.get(username__iexact=username))
        #     (User.objects.get(email__iexact=email))
        #     (User.objects.get(phone_number__iexact=phone_number))
        # except:
        #     return Response("This username has already existed.")
        # except:
        #     return Response("This username has already existed.")
        # except:
        #     return Response("This username has already existed.")
            
            
            
            
                    
            
                    
                
            
        # if NewUser.objects.filter(username=self.cleaned_data['username']).exists():
        #     return Response("username already exists")
        # if NewUser.objects.filter(email=self.cleaned_data['email']).exists():
        #     return Response("username already exists")
        # if NewUser.objects.filter(phone_number=self.cleaned_data['phone_number']).exists():
        #     return Response("username already exists")   
        if (role=="Admin"):
            return Response("can't use admin")   
        ser.save()
        return Response({
            "status": "registered successfully"
        })
        if ser is not None:
            token = Token.objects.create(user=user1)
            return Response(token.key)
        else:
            return Response([], status=status.HTTP_400_BAD_REQUEST)



class UserGet(APIView):
    
    """
    Manager User Login and other things
    """

    permission_classes = (IsAuthenticated,)
    def get(self, request):
        ser = UserSerializered(request.user)
        print("@@@@@@@@@@@@-----@" ,ser)
        return Response(ser.data)
    
class UserPost(APIView):
    
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
        
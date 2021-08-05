from rest_framework import serializers
from user.models import NewUser

class UserSerializered(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = '__all__'
        
        def create(self, validated_data):
    
       
            return CustomUser.objects.create(**validated_data)

        
        
        
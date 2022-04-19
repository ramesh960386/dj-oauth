from django.contrib.auth.models import Group
from rest_framework import serializers
from django.contrib.auth import get_user_model

# class UserSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = User
#         fields = ('email', 'first_name', 'last_name')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'first_name', 'last_name',)
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class GroupSerilizer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('name',)
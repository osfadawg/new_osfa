from rest_framework import serializers
from .models import ExampleModel, OsfaRequests, OsfaUser

class ExampleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExampleModel
        fields = '__all__'

class OsfaUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = OsfaUser
        fields = ['id', 'email', 'first_name', 'last_name']

class OsfaRequestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OsfaRequests
        fields = '__all__'
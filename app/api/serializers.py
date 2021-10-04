import api.models as models
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id']

user = UserSerializer()

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Employee
        fields = ['id', 'status', 'role', 'salary_per_hour', 'hours_per_week', 'user']

class IncomeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Income
        fields = ['id', 'amount', 'description', 'stamp', 'user']

class ExpenseSerializer(serializers.HyperlinkedModelSerializer):
    owner = UserSerializer();
    class Meta:
        model = models.Expense
        fields = ['id', 'amount', 'description', 'stamp', 'owner', 'user']

class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Message
        fields = ['id', 'text', 'stamp', 'user']

class ClientsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Clients
        fields = ['id', 'flow', 'stamp', 'user']

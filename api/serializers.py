from rest_framework import serializers
from api.models import User, Salary

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'cpf', 'date_of_birth')
        cpf = serializers.CharField(max_length=14)

class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Salary
        fields = ('id', 'date', 'value', 'discounts', 'user')


from rest_framework import serializers
from api.models import User, Salary

class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Salary
        fields = ('id', 'date', 'value', 'discounts', 'user')

class UserSerializer(serializers.ModelSerializer):
    salaries = SalarySerializer(many=True)
    class Meta:
        model = User
        fields = ('id', 'name', 'cpf', 'date_of_birth', 'salaries')
        cpf = serializers.CharField(max_length=14)

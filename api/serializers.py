from rest_framework import serializers
from api.models import Company, Result

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'cpf', 'birthday')

class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Salary
        fields = ('id', 'date', 'value', 'discounts', 'user')

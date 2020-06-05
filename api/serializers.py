from rest_framework import serializers
from api.models import User, Salary

class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Salary
        fields = ('id', 'date', 'value', 'discounts', 'user')

class UserSerializer(serializers.ModelSerializer):
    salaries = SalarySerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('id', 'name', 'cpf', 'date_of_birth', 'salaries')
        cpf = serializers.CharField(max_length=14)

class StatisticSerializer(serializers.Serializer):
    avg_salaries = serializers.FloatField()
    avg_discounts = serializers.FloatField()
    max_salary = serializers.FloatField()
    min_salary = serializers.FloatField()


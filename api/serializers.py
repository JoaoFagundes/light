from rest_framework import serializers
from django.db.models import Avg, Max, Min
from api.models import User, Salary

class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Salary
        fields = ('id', 'date', 'value', 'discounts', 'user')

class StatisticSerializer(serializers.Serializer):
    avg_salaries = serializers.FloatField()
    avg_discounts = serializers.FloatField()
    max_salary = serializers.FloatField()
    min_salary = serializers.FloatField()

class UserSerializer(serializers.ModelSerializer):
    salaries = SalarySerializer(many=True, read_only=True)
    statistics = serializers.SerializerMethodField(read_only=True)

    def get_statistics(self, obj):
        statistics = obj.salaries.aggregate(avg_salaries=Avg('value'),
                                            avg_discounts=Avg('discounts'),
                                            max_salary=Max('value'),
                                            min_salary=Min('value'))

        return StatisticSerializer(statistics).data

    class Meta:
        model = User
        fields = ('id', 'name', 'cpf', 'date_of_birth', 'salaries', 'statistics')

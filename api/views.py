from rest_framework import viewsets
from rest_framework.response import Response
from django.db.models import Avg, Max, Min
from api.models import User, Salary
from api.serializers import UserSerializer, SalarySerializer, StatisticSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.select_related()
    serializer_class = UserSerializer

class SalaryViewSet(viewsets.ModelViewSet):
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer

class StatisticViewSet(viewsets.ViewSet):
    serializer_class = StatisticSerializer

    def list(self, request):
        query = Salary.objects.aggregate(avg_salaries=Avg('value'),
                                         avg_discounts=Avg('discounts'),
                                         max_salary=Max('value'),
                                         min_salary=Min('value'))

        return Response(StatisticSerializer(query).data)



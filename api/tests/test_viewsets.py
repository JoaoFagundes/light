import json
from datetime import datetime
from django.urls import reverse
from django.db.models import Avg, Max, Min


from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from ..models import User, Salary
from ..serializers import UserSerializer, SalarySerializer, StatisticSerializer


class UserAPIViewTestCase(APITestCase):
    def setUp(self):
        self.name = "Bilbo Bolseiro"
        self.cpf = "10020030040"
        self.date_of_birth = "1920-09-22"
        self.user = User.objects.create(name=self.name, cpf=self.cpf, date_of_birth=self.date_of_birth)
        self.salary = Salary.objects.create(value=1000, discounts=100, date='2020-06-05', user=self.user)

    def test_user_list(self):
        user_serializer = UserSerializer(self.user)
        salary_serializer = SalarySerializer(self.salary)

        response = self.client.get('/api/v1/users/')
        self.assertEqual(json.loads(response.content)['count'], User.objects.count())
        self.assertEqual(json.loads(response.content)["results"], [user_serializer.data] )
        self.assertEqual(json.loads(response.content)['results'][0]['salaries'], [salary_serializer.data])

    def test_user_retrieve(self):
        user_serializer = UserSerializer(self.user)

        response = self.client.get('/api/v1/users/{}/'.format(self.user.id))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), user_serializer.data)

    def test_create_user(self):
        response = self.client.post('/api/v1/users/',
                                    {"name": "Frodo Bolseiro", "cpf": "50060070080", "date_of_birth":"1950-09-22"})
        self.assertEqual(201, response.status_code)

    def test_update_user(self):
        response = self.client.patch('/api/v1/users/{}/'.format(self.user.id),
                                    {"cpf": "50060070080"})
        self.user.refresh_from_db()
        self.assertEqual(200, response.status_code)
        self.assertEqual(self.user.cpf, "500.600.700-80")

    def test_delete_user(self):
        response = self.client.delete('/api/v1/users/{}/'.format(self.user.id))
        self.assertEqual(204, response.status_code)
        self.assertEqual(User.objects.count(), 0)

class SalaryAPIViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(name='Bilbo Bolseiro', cpf='10020030040', date_of_birth='1970-09-22')
        self.january_salary = Salary.objects.create(value=1000, discounts=100, date='2020-01-05', user=self.user)
        self.february_salary = Salary.objects.create(value=1000, discounts=100, date='2020-02-05', user=self.user)
        self.march_salary = Salary.objects.create(value=1000, discounts=100, date='2020-03-05', user=self.user)

    def test_salary_list(self):
        salary_serializer = SalarySerializer([self.january_salary, self.february_salary, self.march_salary], many=True)

        response = self.client.get('/api/v1/salaries/')
        self.assertEqual(json.loads(response.content)['count'], Salary.objects.count())
        self.assertEqual(json.loads(response.content)["results"], salary_serializer.data)

    def test_salary_retrieve(self):
        salary_serializer = SalarySerializer(self.march_salary)

        response = self.client.get('/api/v1/salaries/{}/'.format(self.march_salary.id))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), salary_serializer.data)

    def test_create_salary(self):
        response = self.client.post('/api/v1/salaries/',
                                    {"date": "2020-04-05",
                                     "value": "1500",
                                     "discounts":"150",
                                     "user": "{}".format(self.user.id)})
        self.assertEqual(201, response.status_code)

    def test_update_salary(self):
        response = self.client.patch('/api/v1/salaries/{}/'.format(self.march_salary.id),
                                    {"value": "1500"})
        self.march_salary.refresh_from_db()
        self.assertEqual(200, response.status_code)
        self.assertEqual(self.march_salary.value, 1500)

    def test_delete_salary(self):
        response = self.client.delete('/api/v1/salaries/{}/'.format(self.march_salary.id))
        self.assertEqual(204, response.status_code)
        self.assertEqual(Salary.objects.count(), 2)


class StatisticsAPIViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(name='Bilbo Bolseiro', cpf='10020030040', date_of_birth='1920-09-22')
        self.user_2 = User.objects.create(name='Frodo Bolseiro', cpf='50060070080', date_of_birth='1970-09-22')
        self.january_salary = Salary.objects.create(value=1000, discounts=100, date='2020-01-05', user=self.user)
        self.february_salary = Salary.objects.create(value=2000, discounts=200, date='2020-02-05', user=self.user)
        self.march_salary = Salary.objects.create(value=1500, discounts=150, date='2020-03-05', user=self.user_2)

    def test_statistics_list(self):
        statistics = Salary.objects.aggregate(avg_salaries=Avg('value'),
                                              avg_discounts=Avg('discounts'),
                                              max_salary=Max('value'),
                                              min_salary=Min('value'))
        statistics_serializer = StatisticSerializer(statistics)

        response = self.client.get('/api/v1/statistics/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), statistics_serializer.data)

    def test_statistics_retrieve(self):
        statistics = Salary.objects.filter(user_id=self.user.id).aggregate(avg_salaries=Avg('value'),
                                                                           avg_discounts=Avg('discounts'),
                                                                           max_salary=Max('value'),
                                                                           min_salary=Min('value'))
        statistics_serializer = StatisticSerializer(statistics)

        response = self.client.get('/api/v1/statistics/{}/'.format(self.user.id))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), statistics_serializer.data)

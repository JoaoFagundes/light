from django.test import TestCase
from api.models import User, Salary
from django.db.utils import DataError

class UserTest(TestCase):
    def setUp(self):
        User.objects.create(name='Leia Organa', cpf='10020030040', date_of_birth='1977-05-25')
        User.objects.create(name='Han Solo', cpf='50060070080', date_of_birth='1977-05-25')

    def test_user_str(self):
        leia = User.objects.get(name='Leia Organa')

        self.assertEqual(str(leia), 'Leia Organa, CPF: 100.200.300-40')

    def test_user_cpf_format(self):
        leia = User.objects.get(name='Leia Organa')
        han = User.objects.get(name='Han Solo')

        self.assertEqual(leia.cpf, '100.200.300-40')
        self.assertEqual(han.cpf, '500.600.700-80')

class SalaryTest(TestCase):
    def setUp(self):
        user = User.objects.create(name='Luke Skywalker', cpf='10020030040', date_of_birth='1977-05-25')
        Salary.objects.create(date='2020-01-05', value='1000', discounts=100, user=user)

    def test_salary_str(self):
        luke = User.objects.get(name='Luke Skywalker')
        january = Salary.objects.get(date='2020-01-05', user=luke)

        self.assertEqual(str(january), 'Salário do(a) Luke Skywalker, CPF: 100.200.300-40 em 05/01/2020.')

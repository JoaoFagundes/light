import re
from django.db import models
from django.core.validators import RegexValidator

class User(models.Model):
    name = models.CharField(max_length=50)
    cpf = models.CharField(max_length=14,
                           validators=[
                               RegexValidator(r'^((\d){3}.?){2}(\d){3}-?(\d){2}$')
                           ])
    date_of_birth = models.DateField()

    def save(self, *args, **kwargs):
        formatted_cpf = re.search("^((\d){3}.){2}(\d){3}-(\d){2}$", self.cpf)
        if not formatted_cpf:
            self.cpf = '{0}.{1}.{2}-{3}'.format(self.cpf[:3],
                                                self.cpf[3:6],
                                                self.cpf[6:9],
                                                self.cpf[9:])

        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return '{}, CPF: {}'.format(self.name, self.cpf)

class Salary(models.Model):
    date = models.DateField()
    value = models.FloatField()
    discounts = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='salaries')

    def __str__(self):
        return 'Salário do(a) {} em {}.'.format(self.user, self.date.strftime("%d/%m/%Y"))

    class Meta:
        verbose_name = "Salary"
        verbose_name_plural = "Salaries"

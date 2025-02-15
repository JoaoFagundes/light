# Generated by Django 2.2.10 on 2020-06-05 14:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='birthday',
            new_name='date_of_birth',
        ),
        migrations.AlterField(
            model_name='user',
            name='cpf',
            field=models.CharField(max_length=14, validators=[django.core.validators.RegexValidator('^((\\d){3}.?){2}(\\d){3}-?(\\d){2}$')]),
        ),
    ]

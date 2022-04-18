# Generated by Django 4.0.4 on 2022-04-18 17:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userregistermodel',
            name='phoneNumber',
            field=models.CharField(max_length=16, unique=True, validators=[django.core.validators.RegexValidator(regex='^09\\d{2}\\s*?\\d{3}\\s*?\\d{4}$')]),
        ),
    ]

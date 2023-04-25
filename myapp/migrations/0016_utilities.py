# Generated by Django 4.1.7 on 2023-04-17 21:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_alter_packages_amount_alter_packages_daily_income_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Utilities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_text', models.TextField(max_length=5000)),
                ('joining_bonus', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
            ],
            options={
                'verbose_name': 'Utilities',
            },
        ),
    ]

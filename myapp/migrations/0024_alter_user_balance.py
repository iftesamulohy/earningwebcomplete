# Generated by Django 4.1.7 on 2023-04-19 20:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0023_alter_completetask_image_alter_completetask_package'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='balance',
            field=models.IntegerField(default=0, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
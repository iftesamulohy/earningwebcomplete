# Generated by Django 4.1.7 on 2023-04-13 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='refferedby',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
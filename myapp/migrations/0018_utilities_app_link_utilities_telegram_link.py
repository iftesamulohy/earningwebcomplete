# Generated by Django 4.1.7 on 2023-04-18 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_alter_utilities_joining_bonus_alter_utilities_n_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='utilities',
            name='app_link',
            field=models.URLField(default='#'),
        ),
        migrations.AddField(
            model_name='utilities',
            name='telegram_link',
            field=models.URLField(default='#'),
        ),
    ]

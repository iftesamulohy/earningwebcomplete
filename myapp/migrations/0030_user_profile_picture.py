# Generated by Django 4.1.7 on 2023-04-25 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0029_packageorder_refferedby'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile'),
        ),
    ]

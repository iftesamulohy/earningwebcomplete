# Generated by Django 4.1.7 on 2023-04-14 17:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_deposit_amount_deposit_date_deposit_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='deposit',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

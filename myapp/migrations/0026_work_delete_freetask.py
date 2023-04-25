# Generated by Django 4.1.7 on 2023-04-19 21:46

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0025_utilities_free_package'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('work_details', models.TextField(max_length=5000)),
                ('work_link', models.URLField(blank=True, null=True)),
                ('reaward_amount', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('starting_date', models.DateField(default=django.utils.timezone.now)),
                ('end_date', models.DateField()),
                ('package', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.packages')),
            ],
        ),
        migrations.DeleteModel(
            name='FreeTask',
        ),
    ]

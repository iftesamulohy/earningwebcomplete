# Generated by Django 4.1.7 on 2023-04-19 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0022_alter_completetask_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completetask',
            name='image',
            field=models.ImageField(upload_to='images/screenshots'),
        ),
        migrations.AlterField(
            model_name='completetask',
            name='package',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.packages'),
        ),
    ]

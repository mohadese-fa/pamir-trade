# Generated by Django 5.1 on 2024-11-20 12:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_rename_city_cityclass'),
    ]

    operations = [
        migrations.AddField(
            model_name='agencyclass',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.cityclass'),
        ),
    ]

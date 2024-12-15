# Generated by Django 5.1 on 2024-11-22 18:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0024_colorclass_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productclass',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='child', to='main_app.categoryclass'),
        ),
    ]
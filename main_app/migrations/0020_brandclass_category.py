# Generated by Django 5.1 on 2024-11-21 16:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0019_questionbclass_questioncclass_questiondclass'),
    ]

    operations = [
        migrations.AddField(
            model_name='brandclass',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.categoryclass'),
        ),
    ]
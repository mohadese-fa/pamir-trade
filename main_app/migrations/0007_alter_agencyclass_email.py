# Generated by Django 5.1 on 2024-11-20 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_agencyclass_telephone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agencyclass',
            name='email',
            field=models.EmailField(blank=True, max_length=50),
        ),
    ]

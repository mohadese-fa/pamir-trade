# Generated by Django 5.1 on 2024-11-22 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0021_remove_brandclass_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoryclass',
            name='text',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]

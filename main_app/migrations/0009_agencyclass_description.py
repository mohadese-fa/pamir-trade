# Generated by Django 5.1 on 2024-11-20 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_alter_agencyclass_phone_alter_agencyclass_photo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='agencyclass',
            name='description',
            field=models.TextField(null=True),
        ),
    ]